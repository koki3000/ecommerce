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

# Order Views

class CreateOrderView(CreateView):
    
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("home")
    template_name = 'mysite/order/create_order_form.html'


    def get_context_data(self, context=None, **kwargs):
        context = super().get_context_data(**kwargs)
        sum = 0
        if not self.request.user.is_anonymous:
            context["order_details"] = OrderDetail.objects.filter(user=self.request.user, order=None)

        delivery = self.request.GET.get('delivery') if self.request.GET.get('delivery') != None else ''
        payment = self.request.GET.get('payment') if self.request.GET.get('payment') != None else ''
        
        if delivery:
            delivery = Delivery.objects.get(pk=delivery)
            sum += delivery.price

        if payment:
            payment = Payment.objects.get(pk=payment)

        for product in context["order_details"]:
            sum += product.price

        if self.request.method == 'POST':
            new_order = Order(user=self.request.user , payment=payment, delivery=delivery)
            new_order.save()
            orders = OrderDetail.objects.filter(user=self.request.user, order=None)
            for order in orders:
                order.order = new_order
                order.save()
            for product in context['order_details']:
                product.product.quantity -= product.quantity
                if product.product.quantity >= 0:
                    product.product.save()
                else:
                    messages.error(self.request, f'Niestety w magazynie mamy tylko {product.quantity} produktu {product.product}.')
            messages.success(self.request, 'Złożono zamówienie.')
            return super().get_context_data(**kwargs)
        
        return super().get_context_data(
            context=context,
            payment=payment,
            delivery=delivery,
            sum=sum,
            **kwargs)
    

class OrderPageView(ListView):

    model = Order
    template_name = 'mysite/order/order_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(user=self.request.user)

        return context
    

class OrderContentView(ListView):

    model = OrderDetail
    template_name = 'mysite/order/order_content.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        sum = 0
        context["order"] = Order.objects.get(pk=self.kwargs['pk'])
        context["order_detail_list"] = OrderDetail.objects.filter(order=self.kwargs['pk'])

        for product in context["order_detail_list"]:
            sum += product.price
        sum += context["order"].delivery.price
        
        context["sum"] = sum

        return context