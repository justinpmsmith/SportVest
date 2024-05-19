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
                # print(queryset.description)

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
        info['receipt_no'] = timestamp

        if info:
            # Utils.updateDb(info)

            # send digital receipt
            receipt_info = {
                'receipt_no': timestamp,
                'total_price': info['totalPrice'],
                'customer_name': info['name'],
                # 'delivery_type': info['deliveryMethod'],
                'delivery_location': info['address'],
                'shipping_fee': info['shipping_fee'],
            }
            pdf_receipt = Utils.generateReceipt(info['products'], receipt_info)
            Utils.emailReceipt(pdf_receipt, info)
            print("email sent")

        return Response({'message': 'success'})


class ContactUS(APIView):
    def post(self, request):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        info = request.data  # or request.json(), depending on your setup
        print(info)
        Utils.emailContactUsMessage(info)
        return Response({'message': 'success'})
