from django.urls import path
from ..views import order_details

urlpatterns = [
    path('order_detail/', order_details.OrderDetailPageView.as_view(), name="order_detail"),
    path('order_detail/<int:pk>/delete/', order_details.DeleteOrderDetailView.as_view(), name="delete-order_detail"),
    path('order_detail/delete-all/', order_details.delete_all_order_detail, name="delete-all-order_detail"),
    path('order_detail/<int:pk>/update/', order_details.UpdateOrderDetailView.as_view(), name="update-order_detail"),
    path('order_detail/buy/', order_details.buy_view, name="buy-order_detail"),
]