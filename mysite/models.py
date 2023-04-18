from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price =  models.FloatField()
    category = models.ForeignKey(Category, models.PROTECT, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    availability = models.BooleanField()
    quantity = models.IntegerField()