from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('heritage.urls')),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('users/',include('django.contrib.auth.urls')),
]
