from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import path, reverse_lazy, reverse
from . models import Product, Category, Basket
from . forms import ProductForm, CategoryForm, UserForm, BasketForm
from django.contrib.auth.models import User


# Create your views here.


# Product Views

class HomePageView(ListView):

    model = Product
    template_name = 'mysite/product/product_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


class ProductView(CreateView):
    
    model = Basket
    form_class = BasketForm
    success_url = reverse_lazy("home")
    template_name = 'mysite/product/detail_product.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.get(pk=self.kwargs['pk'])
        return context
    

    def form_valid(self, form):
        data = form.save(commit=False)
        if not self.request.user.is_anonymous:
            data.owner = self.request.user
        data.product = Product.objects.get(pk=self.kwargs['pk'])
        data.save()
        return super(ProductView, self).form_valid(form)


class CreateProductView(CreateView):

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("home")
    template_name = 'mysite/product/create_product_form.html'


class DeleteProductView(DeleteView):

    model = Product
    success_url = reverse_lazy("home")
    template_name = 'mysite/product/delete_product_form.html'


class UpdateProductView(UpdateView):

    model = Product
    form_class = ProductForm
    template_name = 'mysite/product/update_product_form.html'


    def get_success_url(self):
        return reverse('details-product', kwargs={'pk': self.object.id})
    

# Category Views

class CategoryPageView(ListView):

    model = Category
    template_name = 'mysite/category/category_list.html'
    

class CategoryView(DetailView):
    
    model = Category
    template_name = 'mysite/category/detail_category.html'


class CreateCategoryView(CreateView):

    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("category")
    template_name = 'mysite/category/create_category_form.html'


class DeleteCategoryView(DeleteView):

    model = Category
    success_url = reverse_lazy("category")
    template_name = 'mysite/category/delete_category_form.html'


class UpdateCategoryView(UpdateView):

    model = Category
    form_class = CategoryForm
    template_name = 'mysite/category/update_category_form.html'


    def get_success_url(self):
        return reverse('details-category', kwargs={'pk': self.object.id})


# User Views

class CreateUser(CreateView):    
    model = User
    form_class = UserForm
    template_name = 'mysite/user_create_form.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        data = form.save(commit=False)
        data.set_password(data.password)
        data.save()
        return super(CreateUser, self).form_valid(form)


# Basket Views

class BasketPageView(ListView):

    model = Basket
    template_name = 'mysite/basket_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('user: ', self.request.user.is_anonymous)
        print(context)
        if not self.request.user.is_anonymous:
            print('cos')
            context["basket_product_list"] = Basket.objects.filter(owner = self.request.user)
        return context