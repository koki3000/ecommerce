from django.urls import path
from ..views import product

urlpatterns = [
    path('', product.HomePageView.as_view(), name="home"),
    path('product/create/', product.CreateProductView.as_view(), name="create-product"),
    path('product/<int:pk>/delete/', product.DeleteProductView.as_view(), name="delete-product"),
    path('product/<int:pk>/update/', product.UpdateProductView.as_view(), name="update-product"),
    path('product/<int:pk>/', product.ProductView.as_view(), name="details-product"),
    path('slider/<str:name>/', product.slider_view, name="slider"),
]