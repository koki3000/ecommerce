from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import path, reverse_lazy, reverse
from . models import Product, Category, OrderDetail, Delivery, Payment
from . forms import ProductForm, CategoryForm, UserForm, OrderDetailForm, ProductSearchForm, DeliveryForm, PaymentForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


# Create your views here.


# Product Views

class HomePageView(ListView):

    model = Product
    template_name = 'mysite/product/product_list.html'
    
    def get_context_data(self, context=None, **kwargs):
        context = super().get_context_data(**kwargs)
        sort = None
        form = ProductSearchForm(self.request.GET)
        if form.is_valid():
            sort = form.cleaned_data.get('sort', '')
            
            if form.cleaned_data.get('name', ''):
                
                name = form.cleaned_data.get('name', '').strip()
                if name:
                    context["product_list"] = context["product_list"].filter(name__icontains=name)

        category = self.request.GET.get('category') if self.request.GET.get('category') != None else ''
        if category:
            context["one_category"] = Category.objects.get(pk=category)
            context["product_list"] = context["product_list"].filter(category=category)
        else:
            context["category_list"] = Category.objects.all()

        if sort:
            context["product_list"] = context["product_list"].order_by(sort)

        return super().get_context_data(
            form=form,
            context=context,
            **kwargs)


class ProductView(CreateView):
    
    model = OrderDetail
    form_class = OrderDetailForm
    success_url = reverse_lazy("home")
    template_name = 'mysite/product/detail_product.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.get(pk=self.kwargs['pk'])
        return context
    

    def form_valid(self, form):
        data = form.save(commit=False)
        
        if not self.request.user.is_anonymous:
            data.user = self.request.user
        data.product = Product.objects.get(pk=self.kwargs['pk'])
        user = data.user
        product = data.product
        quantity = data.quantity
        if OrderDetail.objects.filter(product=product, user=user).exists():
            data = OrderDetail.objects.get(product=product, user=user)
            data.quantity += quantity
        if data.quantity > data.product.quantity:
            messages.error(self.request,  f'W magazynie mamy tylko {data.product.quantity} sztuk tego towaru.')
            order_detail_item = self.request.POST.get('order_detail_item', f'/product/{data.product.id}/')
            return HttpResponseRedirect(order_detail_item)
        data.save()
        messages.success(self.request, f'Produkt {product} dodany do koszyka.')
        home = self.request.POST.get('home', '/')
        return HttpResponseRedirect(home)


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


# OrderDetail Views

class OrderDetailPageView(ListView):

    model = OrderDetail
    template_name = 'mysite/order_detail/order_detail_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sum = 0
        action = self.request.GET.get('action') if self.request.GET.get('action') != None else ''
        order_detail_id = int(self.request.GET.get('order_detail_id')) if self.request.GET.get('order_detail_id') != None else ''

        if action == 'plus' and order_detail_id:
            order_detail_obj = OrderDetail.objects.get(pk=order_detail_id)
            order_detail_obj.quantity += 1
            if order_detail_obj.quantity > order_detail_obj.product.quantity:
                messages.error(self.request,  f'W magazynie mamy tylko {order_detail_obj.product.quantity} sztuk tego towaru.')
            else:
                order_detail_obj.save()
        elif action == 'minus' and order_detail_id:
            order_detail_obj = OrderDetail.objects.get(pk=order_detail_id)
            order_detail_obj.quantity -= 1
            if order_detail_obj.quantity == 0:
                order_detail_obj.delete()
            else:
                order_detail_obj.save()

        if not self.request.user.is_anonymous:
            context["order_detail_product_list"] = OrderDetail.objects.filter(user = self.request.user)

        for product in context["order_detail_product_list"]:
            sum += product.price

        context["sum"] = sum

        return context
    

class DeleteOrderDetailView(DeleteView):

    model = OrderDetail
    success_url = reverse_lazy("order_detail")
    template_name = 'mysite/order_detail/delete_order_detail_form.html'
    

def delete_all_order_detail(request):

    order_detail = OrderDetail.objects.filter(user = request.user)
    context = {'order_detail_list': order_detail}    
    
    if request.method == 'GET':
        return render(request, 'mysite/order_detail/delete_all_order_detail_form.html',context)
    if request.method == 'POST':
        order_detail.delete()
        messages.success(request,  'Koszyk został opróżniony.')
        home = request.POST.get('home', '/')
        return HttpResponseRedirect(home)
    

class UpdateOrderDetailView(UpdateView):

    model = OrderDetail
    form_class = OrderDetailForm
    success_url = reverse_lazy("order_detail")
    template_name = 'mysite/order_detail/update_order_detail_form.html'

    def form_valid(self, form):
        data = form.save(commit=False)
        if data.quantity > data.product.quantity:
            messages.error(self.request,  f'W magazynie mamy tylko {data.product.quantity} sztuk tego towaru.')
            order_detail_item = self.request.POST.get('order_detail_item', f'/order_detail/{data.id}/update/')
            return HttpResponseRedirect(order_detail_item) 
        return super().form_valid(form)
    

def buy_view(request):
    order_detail = OrderDetail.objects.filter(user = request.user)
    context = {'order_detail_list': order_detail}

    if request.method == 'GET':
        return render(request, 'mysite/order_detail/buy_form.html',context)
    if request.method == 'POST':
        for product in context['order_detail_list']:
            product.product.quantity -= product.quantity
            if product.product.quantity >= 0:
                product.product.save()
                product.delete()
            else:
                messages.error(request, f'Niestety w magazynie mamy tylko {product.quantity} produktu {product.product}.')
        messages.success(request, f'Produkty zamówione.')
        home = request.POST.get('home', '/')
        return HttpResponseRedirect(home)
    

# Delivery Views

class DeliveryPageView(ListView):

    model = Delivery
    template_name = 'mysite/delivery/delivery_list.html'
    

class DeliveryView(DetailView):
    
    model = Delivery
    template_name = 'mysite/delivery/detail_delivery.html'


class CreateDeliveryView(CreateView):

    model = Delivery
    form_class = DeliveryForm
    success_url = reverse_lazy("delivery")
    template_name = 'mysite/delivery/create_delivery_form.html'


class DeleteDeliveryView(DeleteView):

    model = Delivery
    success_url = reverse_lazy("delivery")
    template_name = 'mysite/delivery/delete_delivery_form.html'


class UpdateDeliveryView(UpdateView):

    model = Delivery
    form_class = DeliveryForm
    template_name = 'mysite/delivery/update_delivery_form.html'


    def get_success_url(self):
        return reverse('details-delivery', kwargs={'pk': self.object.id})
    

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