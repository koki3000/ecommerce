from django.urls import path
from ..views import order

urlpatterns = [
    path('order/create/', order.CreateOrderView.as_view(), name="create-order"),
    path('order/', order.OrderPageView.as_view(), name="order"),
    path('order/content/<int:pk>/', order.OrderContentView.as_view(), name="content-order"),
]