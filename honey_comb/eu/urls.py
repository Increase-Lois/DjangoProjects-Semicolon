from django.urls import path
from django.http import HttpResponse
from . import views




urlpatterns = [
    path('register',views.eu_register),
    path('login',views.eu_login)
]