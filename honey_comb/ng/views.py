from django.shortcuts import render

# Create your views here.

def ng_register(request):
    return render(request,"register.html" ,context={"country": "Nigerian"})

def ng_login(request):
    return render(request, "login.html", context={"country": "Nigerian"})
