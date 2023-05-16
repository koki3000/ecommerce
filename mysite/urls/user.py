from django.urls import path
from ..views import user

urlpatterns = [
    path('user/create/', user.CreateUser.as_view(), name="create-user"),
    path('contact/', user.contact_view, name="contact"),
]