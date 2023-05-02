from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):

    name = models.CharField('Nazwa', max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField('Nazwa', max_length=50, null=True, blank=True)
    price =  models.FloatField('Cena', validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, models.PROTECT, 'Kategoria', null=True, blank=True)
    description = models.TextField('Opis', null=True, blank=True)
    availability = models.BooleanField('Dostępność')
    quantity = models.PositiveIntegerField('Ilość w magazynie')

    def __str__(self):
        return f'{self.name}'


class Basket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, models.PROTECT, 'Produkt', null=True, blank=True)
    quantity = models.PositiveIntegerField('Ilość', validators=[MinValueValidator(1)], null=True, blank=True, default=1)

    @property
    def price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f'{self.product}'


class Delivery(models.Model):
    name = models.CharField('Nazwa', max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'
    
    
class Payment(models.Model):
    payment_type = models.CharField('Typ płatności', max_length=50, unique=True)

    def __str__(self):
        return f'{self.payment_type}'