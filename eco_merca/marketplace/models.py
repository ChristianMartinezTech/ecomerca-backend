from django.db import models


class Brand(models.Model):
    #brand_id = models.IntegerField
    name = models.CharField(max_length=50)
    product_quantity = models.IntegerField
    instagram = models.CharField(max_length=100)

    # String method
    def __str__(self):
        return self.name


class Product(models.Model):
    #product_id = models.IntegerField
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField
    price = models.FloatField
    quantity = models.IntegerField

    # String method
    def __str__(self):
        return str(self.brand_id) + self.name + self.description + str(self.price) + str(self.quantity)