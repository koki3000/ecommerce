from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from .. models import OrderDetail
from .. forms import OrderDetailForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# OrderDetail Views

class OrderDetailPageView(ListView):

    model = OrderDetail
    template_name = 'mysite/order_detail/order_detail_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
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
                context["order_detail_product_list"] = OrderDetail.objects.filter(user = self.request.user, order = None)

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