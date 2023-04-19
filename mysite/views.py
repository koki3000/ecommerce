from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import path, reverse_lazy, reverse
from . models import Product
from . forms import ProductForm


# Create your views here.


class HomePageView(ListView):

    model = Product

class CreateProductView(CreateView):

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("home")
    template_name = 'mysite/create_product_form.html'
