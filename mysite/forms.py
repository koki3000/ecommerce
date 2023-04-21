from django.forms import ModelForm
from .models import Product, Category, Basket
from django.contrib.auth.models import User


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class BasketForm(ModelForm):
    class Meta:
        model = Basket
        fields = ['quantity']