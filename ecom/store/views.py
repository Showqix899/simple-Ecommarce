from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from django.contrib.auth import logout,login,authenticate
# Create your views here.

#view for home page
def home(request):
    products=Products.objects.all() # fetching all the products from the database
    return render (request,'index.html',{'products':products})

#about page

def about(request):

    return render(request,'about.html',{})

def login_user(request):
    return render(request,'login.html',{})