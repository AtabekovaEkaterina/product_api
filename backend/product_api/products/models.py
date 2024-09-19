from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
