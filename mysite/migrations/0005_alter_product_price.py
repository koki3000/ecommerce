# Generated by Django 4.2 on 2023-04-19 18:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
