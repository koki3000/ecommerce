from django.urls import path
from . import views
from . models import Product

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('product/create/', views.CreateProductView.as_view(), name="create-product")
]