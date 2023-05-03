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
    path('order_detail/', views.OrderDetailPageView.as_view(), name="order_detail"),
    path('order_detail/<int:pk>/delete/', views.DeleteOrderDetailView.as_view(), name="delete-order_detail"),
    path('order_detail/delete-all/', views.delete_all_order_detail, name="delete-all-order_detail"),
    path('order_detail/<int:pk>/update/', views.UpdateOrderDetailView.as_view(), name="update-order_detail"),
    path('order_detail/buy/', views.buy_view, name="buy-order_detail"),
    path('delivery/create/', views.CreateDeliveryView.as_view(), name="create-delivery"),
    path('delivery/<int:pk>/delete/', views.DeleteDeliveryView.as_view(), name="delete-delivery"),
    path('delivery/<int:pk>/update/', views.UpdateDeliveryView.as_view(), name="update-delivery"),
    path('delivery/<int:pk>/', views.DeliveryView.as_view(), name="details-delivery"),
    path('delivery/', views.DeliveryPageView.as_view(), name="delivery"),
]