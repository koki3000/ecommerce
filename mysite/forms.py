from django.forms import ModelForm
from .models import Product, Category, OrderDetail, Delivery, Payment
from django.contrib.auth.models import User
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


SORT_CHOICES =(
    ("name", "a-z"),
    ("-name", "z-a"),
    ("price", "po cenie rosnąco"),
    ("-price", "po cenie malejąco"),
)

class ProductSearchForm(ModelForm):

    sort = forms.ChoiceField(choices=SORT_CHOICES, label="Sortuj")
    sort.required = False
    class Meta:
        model = Product

        fields = ('name', 'category', )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].required = False
            


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class OrderDetailForm(ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['quantity']


class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'