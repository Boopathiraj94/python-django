from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=250)
    rate = models.FloatField(default=0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name 