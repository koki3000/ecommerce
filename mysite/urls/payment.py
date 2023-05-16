from django.urls import path
from ..views import payment

urlpatterns = [
    path('payment/create/', payment.CreatePaymentView.as_view(), name="create-payment"),
    path('payment/<int:pk>/delete/', payment.DeletePaymentView.as_view(), name="delete-payment"),
    path('payment/<int:pk>/update/', payment.UpdatePaymentView.as_view(), name="update-payment"),
    path('payment/<int:pk>/', payment.PaymentView.as_view(), name="details-payment"),
    path('payment/', payment.PaymentPageView.as_view(), name="payment"),
]