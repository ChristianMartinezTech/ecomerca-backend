from django.db import models


class Brand(models.Model):
    #brand_id = models.IntegerField
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default="remoto")
    product_quantity = models.IntegerField(default=0)
    instagram = models.CharField(max_length=100)

    # String method
    def __str__(self):
        return f'Brand name:{self.name} - Product Quantity:{self.product_quantity} - Contact:@{self.instagram}'


class Product(models.Model):
    #product_id = models.IntegerField
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    #image = models.ImageField

    # String method
    def __str__(self):
        return f'brand id:{self.brand_id} - Product Name:{self.name} - Price:{self.price} - Quantity:{self.quantity}'