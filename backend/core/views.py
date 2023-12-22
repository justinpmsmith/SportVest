from rest_framework.decorators import api_view

from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import viewsets, status
from .serializers import ProductSerializer
from .models import Product


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

        subject = 'New Product'
        message = f"Description: {description}\nPrice: {price}\nCell: {cell} \nEmail: {email_addr}"
        from_email = settings.EMAIL_HOST_USER
        to_email = ['justinpmsmith10@gmail.com']

        # email = EmailMessage(subject, message, from_email, to_email)
        #
        # # Attach the images to the email
        # for image in images:
        #     email.attach(image.name, image.read(), image.content_type)
        #
        # # Send the email
        # email.send()
        #
        # print("################  Emial sent    ####################")

        return Response({'message': 'success'})


