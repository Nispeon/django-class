from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=500)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

