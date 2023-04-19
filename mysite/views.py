from django.views.generic.list import ListView
from . models import Product

# Create your views here.

class HomePageView(ListView):

    model = Product