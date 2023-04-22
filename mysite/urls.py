from django.urls import path
from . import views
from . models import Product

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('product/create/', views.CreateProductView.as_view(), name="create-product"),
    path('product/<int:pk>/delete/', views.DeleteProductView.as_view(), name="delete-product"),
    path('product/<int:pk>/update/', views.UpdateProductView.as_view(), name="update-product"),
    path('product/<int:pk>/', views.ProductView.as_view(), name="details-product"),
    path('category/create/', views.CreateCategoryView.as_view(), name="create-category"),
    path('category/<int:pk>/delete/', views.DeleteCategoryView.as_view(), name="delete-category"),
    path('category/<int:pk>/update/', views.UpdateCategoryView.as_view(), name="update-category"),
    path('category/<int:pk>/', views.CategoryView.as_view(), name="details-category"),
    path('category/', views.CategoryPageView.as_view(), name="category"),
    path('user/create/', views.CreateUser.as_view(), name="create-user"),
    path('basket/', views.BasketPageView.as_view(), name="basket"),
]