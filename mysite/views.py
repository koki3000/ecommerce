from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import path, reverse_lazy, reverse
from . models import Product, Category
from . forms import ProductForm


# Create your views here.


class HomePageView(ListView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context
    

class ProductView(DetailView):
    
    model = Product
    template_name = 'mysite/detail_product.html'

class CreateProductView(CreateView):

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("home")
    template_name = 'mysite/create_product_form.html'


class DeleteProductView(DeleteView):

    model = Product
    success_url = reverse_lazy("home")
    template_name = 'mysite/delete_product_form.html'


class UpdateProductView(UpdateView):

    model = Product
    form_class = ProductForm
    template_name = 'mysite/update_product_form.html'


    def get_success_url(self):
        return reverse('details-product', kwargs={'pk': self.object.id})