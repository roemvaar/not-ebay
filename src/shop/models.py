from django.db import models
from django.conf import settings
import datetime


class Product(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.product_name
