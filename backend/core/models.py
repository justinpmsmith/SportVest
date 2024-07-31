from django.db import models


# Create your models here.

class Product(models.Model):
    CATEGORIES = (
        ('Cricket', 'Cricket'),
        ('Hockey', 'Hockey'),
        ('Athletics', 'Athletics'),
        ('Soccer', 'Soccer'),
        ('Rugby', 'Rugby'),
        ('Golf', 'Golf'),
        ('Tennis', 'Tennis'),
        ('Horse_Riding', 'Horse_Riding'),
        ('Other', 'Other'),
        ('Cycling', 'Cycling'),
        ('Trainers', 'Trainers'),

    )

    name = models.CharField(max_length=120)
    prodCode = models.CharField(max_length=10)
    category = models.CharField(choices=CATEGORIES, max_length=20)
    description = models.TextField(default="")
    image = models.FileField(default="")
    image2 = models.FileField(default="", blank=True, null=True)
    image3 = models.FileField(default="", blank=True, null=True)

    shoes = models.BooleanField(default=False)
    price = models.FloatField(default=9999)

    def __str__(self):
        return self.prodCode + " - " + self.name


class Receipt(models.Model):
    receiptNo = models.CharField(max_length=120)
    buyerName = models.CharField(max_length=120)
    cell = models.CharField(max_length=13)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    totalPrice = models.FloatField(default=9999)

    def __str__(self):
        return self.receiptNo + " - " + self.buyerName


class Sold(models.Model):
    prodName = models.CharField(max_length=120)
    prodCode = models.CharField(max_length=10)
    price = models.FloatField(default=9999)
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, default=None)
    receiptNo = models.CharField(max_length=120)


    def __str__(self):
        return self.prodCode + " - " + self.receiptNo
