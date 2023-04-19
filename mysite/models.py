from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price =  models.FloatField(validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, models.PROTECT, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    availability = models.BooleanField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'


class Basket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.product}'