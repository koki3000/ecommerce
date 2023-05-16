from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from .. models import Delivery
from .. forms import DeliveryForm
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