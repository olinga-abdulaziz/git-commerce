from django.db import models

# Create your models here.
class Product(models.Model):
    product=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    quantity=models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2,max_digits=7)

    def __str__(self):
        return self.product
