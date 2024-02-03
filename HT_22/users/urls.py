from django.urls import path
from django.urls import include
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('users/', include('django.contrib.auth.urls')),
]
