from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from .. models import Product, Category, OrderDetail
from .. forms import ProductForm, OrderDetailForm, ProductSearchForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Product Views

class HomePageView(ListView):

    model = Product
    template_name = 'mysite/product/product_list.html'
    
    def get_context_data(self, context=None, **kwargs):
        context = super().get_context_data(**kwargs)
        sort = None
        category_list = []
        context["category_list"] = None
        form = ProductSearchForm(self.request.GET)
        if form.is_valid():
            sort = form.cleaned_data.get('sort', '')
            
            if form.cleaned_data.get('name', ''):
                
                name = form.cleaned_data.get('name', '').strip()
                if name:
                    context["product_list"] = context["product_list"].filter(name__icontains=name)
                    for product in context["product_list"]:
                        category_name = product.category.name
                        if category_name not in category_list:
                            category_list.append(category_name)

                    context["category_list"] = Category.objects.filter(name__in=category_list)                        

        category = self.request.GET.get('category') if self.request.GET.get('category') != None else ''
        if category:
            context["one_category"] = Category.objects.get(pk=category)
            context["product_list"] = context["product_list"].filter(category=category)
        elif not context["category_list"]:
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
        if OrderDetail.objects.filter(product=product, user=user, order=None).exists():
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
    
    
def slider_view(request, name):
    product = Product.objects.get(name=name)
    path = f'/product/{product.id}/'
    return HttpResponseRedirect(path)