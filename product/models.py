from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    categories = models.ForeignKey(Category, related_name='products')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
