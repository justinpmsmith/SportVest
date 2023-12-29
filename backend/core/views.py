from rest_framework.decorators import api_view

from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets, status
from .serializers import ProductSerializer
from .models import Product, Sold, Receipt
from datetime import datetime
from .utils import Utils


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        category = self.request.query_params.get('category', None)
        if category is not None and category != 'all':
            if category.lower() == 'shoes':
                queryset = queryset.filter(shoes=True)
            else:
                queryset = queryset.filter(category=category)

        return queryset


class SellSomethingForm(APIView):
    # serializer_class = FormSerializer

    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        description = request.data.get('description')
        price = request.data.get('price')
        cell = request.data.get('cell')
        email_addr = request.data.get('email')

        images = request.FILES.getlist('images')

        subject = 'New Product ' + email_addr
        message = f"Description: {description}\nPrice: {price}\nCell: {cell} \nEmail: {email_addr}"
        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.ADMIN_EMAIL]

        email = EmailMessage(subject, message, from_email, to_email)

        # Attach the images to the email
        for image in images:
            email.attach(image.name, image.read(), image.content_type)

        # Send the email
        email.send()

        print("################  Email sent    ####################")

        return Response({'message': 'success'})


class SoldItems(APIView):
    # serializer_class = FormSerializer

    # Python backend view or API endpoint
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        info = request.data  # or request.json(), depending on your setup
        timestamp = datetime.now()

        if info:
            print(info['products'])

            products = info['products']
            # add to receipts table
            receipt_entry = Receipt(receiptNo=timestamp,
                                    buyerName=info['name'],
                                    cell=info['cell'],
                                    email=info['email'],
                                    address=info['address'],
                                    totalPrice=info['totalPrice'])
            receipt_entry.save()
            for product in products.values():
                # remove Product from Produtcs table
                db_product = Product.objects.get(prodCode=product['prodCode'])
                db_product.delete()

                # add to Sold table
                sold_entry = Sold(prodName=product['name'],
                                  prodCode=product['prodCode'],
                                  price=product['price'],
                                  receipt=receipt_entry,
                                  receiptNo=timestamp)
                sold_entry.save()

            # send digital receipt
            pdf_receipt = Utils.generateReceipt(info['products'], timestamp, info['totalPrice'])

            subject = f"SportVest receipt {timestamp}"
            message = f"Dear {info['name']}, \n\n Thank you for your purchase " \
                      f"\n\n please confirm that the delivery information we have for this order is correct " \
                      f"\n\n Location: PEP or Postnet at {info['address']}" \
                      f"\n Contact Cell: {info['cell']}" \
                      f"\n\n If there are any problems please contact Cherise at {settings.ADMIN_EMAIL }" \
                      f"Thank you for your support"

            from_email = settings.EMAIL_HOST_USER
            to_email = [settings.ADMIN_EMAIL, info['email']]

            email = EmailMessage(subject, message, from_email, to_email)

            # Attach the PDF to the email
            email.attach('receipt.pdf', pdf_receipt, 'application/pdf')

            # Send the email
            email.send()
        return Response({'message': 'success'})
