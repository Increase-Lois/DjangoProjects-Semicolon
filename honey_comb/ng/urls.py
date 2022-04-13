
from django.urls import path
from django.http import HttpResponse
from .import views






urlpatterns = [
    path('register', views.ng_register),
    path('login', views.ng_login)
]