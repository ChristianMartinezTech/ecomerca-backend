from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    instagram_nickname = models.CharField(max_length=50)
    amount_of_products  = models.IntegerField

    def __str__(self):
        return f'Brand name:{self.name} - Contact:@{self.instagram_nickname}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=240)
    image = models.ImageField(upload_to="uploads/")
    price = models.FloatField
    amount = models.IntegerField
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name:{self.name} - Description:{self.description} - Price:{self.price}'
    