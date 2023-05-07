from django.forms import ModelForm
from .models import Product, Category, OrderDetail, Delivery, Payment, Order
from django.contrib.auth.models import User
from django import forms


SORT_CHOICES =(
    ("name", "a-z"),
    ("-name", "z-a"),
    ("price", "po cenie rosnąco"),
    ("-price", "po cenie malejąco"),
)


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductSearchForm(ModelForm):

    sort = forms.ChoiceField(choices=SORT_CHOICES, label="Sortuj")
    sort.required = False
    class Meta:
        model = Product

        fields = ('name', 'category', )

    def __init__(self, *args, **kwargs):
        super(ProductSearchForm, self).__init__(*args, **kwargs)        
        self.fields['category'].label = "Kategoria"            


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


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ('delivery', 'payment', )
    
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['delivery'].label = "Sposób dostawy"
        self.fields['payment'].label = "Sposób płatności"