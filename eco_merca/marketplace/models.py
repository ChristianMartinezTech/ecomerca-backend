from django.db import models


class Brand(models.Model):
    #brand_id = models.IntegerField
    name = models.CharField(max_length=50)
    product_quantity = models.IntegerField
    instagram = models.CharField(max_length=100)

    # String method
    def _str_(self):
        return f'Brand name:{self.name} - Product Quantity:{self.product_quantity} - Contact:@{self.instagram}'


class Product(models.Model):
    #product_id = models.IntegerField
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField()
    price = models.FloatField()
    quantity = models.IntegerField()

    # String method
    def _str_(self):
        return f'brand id:{self.brand_id} - Product Name:{self.name} - Quantity:{self.quantity}'
