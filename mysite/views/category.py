from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import path, reverse_lazy, reverse
from .. models import Product, Category, OrderDetail, Delivery, Payment, Order
from .. forms import ProductForm, CategoryForm, UserForm, OrderDetailForm, ProductSearchForm, DeliveryForm, PaymentForm, OrderForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

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