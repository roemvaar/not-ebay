from django.db import models
from django.conf import settings
from django.utils import timezone


class Product(models.Model):
    seller = models.ForeignKey('auth.User')
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.product_name
