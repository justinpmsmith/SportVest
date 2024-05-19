

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', "prodCode", 'category', "image", "price", "description")


# class FormSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PendingProduct
#         fields = ('description', 'price', 'cell', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6')




