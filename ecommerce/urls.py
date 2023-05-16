from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('mysite.urls')),
    path('', include('mysite.urls.category')),
    path('', include('mysite.urls.delivery')),
    path('', include('mysite.urls.order_details')),
    path('', include('mysite.urls.order')),
    path('', include('mysite.urls.payment')),
    path('', include('mysite.urls.product')),
    path('', include('mysite.urls.user')),
    path('accounts/', include('django.contrib.auth.urls')),
]
