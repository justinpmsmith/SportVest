from django.contrib import admin

from .models import Product, Sold, Receipt


# Register your models here.

admin.site.register(Product)
admin.site.register(Sold)
admin.site.register(Receipt)

