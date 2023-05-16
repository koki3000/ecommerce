from django.urls import path
from ..views import delivery

urlpatterns = [
    path('delivery/create/', delivery.CreateDeliveryView.as_view(), name="create-delivery"),
    path('delivery/<int:pk>/delete/', delivery.DeleteDeliveryView.as_view(), name="delete-delivery"),
    path('delivery/<int:pk>/update/', delivery.UpdateDeliveryView.as_view(), name="update-delivery"),
    path('delivery/<int:pk>/', delivery.DeliveryView.as_view(), name="details-delivery"),
    path('delivery/', delivery.DeliveryPageView.as_view(), name="delivery"),
]