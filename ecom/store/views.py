from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.

#view for home page
def home(request):
    products=Products.objects.all() # fetching all the products from the database
    return render (request,'index.html',{'products':products})