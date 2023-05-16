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


def contact_view(request):
    return render(request, 'mysite/contact.html')