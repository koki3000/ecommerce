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

# Payment Views

class PaymentPageView(ListView):

    model = Payment
    template_name = 'mysite/payment/payment_list.html'
    

class PaymentView(DetailView):
    
    model = Payment
    template_name = 'mysite/payment/detail_payment.html'


class CreatePaymentView(CreateView):

    model = Payment
    form_class = PaymentForm
    success_url = reverse_lazy("payment")
    template_name = 'mysite/payment/create_payment_form.html'


class DeletePaymentView(DeleteView):

    model = Payment
    success_url = reverse_lazy("payment")
    template_name = 'mysite/payment/delete_payment_form.html'


class UpdatePaymentView(UpdateView):

    model = Payment
    form_class = PaymentForm
    template_name = 'mysite/payment/update_payment_form.html'


    def get_success_url(self):
        return reverse('details-payment', kwargs={'pk': self.object.id})