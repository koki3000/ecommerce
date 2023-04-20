from django.urls import path
from . import views
from . models import Product

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('product/create/', views.CreateProductView.as_view(), name="create-product"),
    path('product/<int:pk>/delete/', views.DeleteProductView.as_view(), name="delete-product"),
    path('product/<int:pk>/update/', views.UpdateProductView.as_view(), name="update-product"),
    path('product/<int:pk>/', views.ProductView.as_view(), name="details-product"),
]