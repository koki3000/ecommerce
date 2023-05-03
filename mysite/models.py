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
    
    
class Delivery(models.Model):
    name = models.CharField('Nazwa', max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'
    
    
class Payment(models.Model):
    payment_type = models.CharField('Typ płatności', max_length=50, unique=True)

    def __str__(self):
        return f'{self.payment_type}'
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey(Payment, models.PROTECT, 'Płatność', null=True, blank=True)
    order_date = models.DateField('Data zamówienia', null=True, blank=True)
    ship_date = models.DateField('Data nadania', null=True, blank=True)
    required_date = models.DateField('Data dostarczenia', null=True, blank=True)
    delivery = models.ForeignKey(Delivery, models.PROTECT, 'Dostawa', null=True, blank=True)
    paid = models.BooleanField('Opłacono')
    payment_date = models.DateField('Data płatności', null=True, blank=True)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, models.PROTECT, 'Zamówienie', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, models.PROTECT, 'Produkt', null=True, blank=True)
    quantity = models.PositiveIntegerField('Ilość', validators=[MinValueValidator(1)], null=True, blank=True, default=1)
    total = models.FloatField('Suma', validators=[MinValueValidator(0)], null=True, blank=True,)

    @property
    def price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f'{self.product}'