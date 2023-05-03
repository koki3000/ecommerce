# Generated by Django 4.2 on 2023-04-28 09:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_alter_basket_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='price',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cena'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basket',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Produkt', to='mysite.product'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Ilość'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.BooleanField(verbose_name='Dostępność'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Kategoria', to='mysite.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cena'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Ilość w magazynie'),
        ),
    ]