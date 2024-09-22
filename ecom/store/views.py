from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products,Catagory
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from .forms import SignUpForm
from django.db.models import Q
# Create your views here.

#view for home page
def home(request):
    q=request.GET.get('q','')
    catagories=Catagory.objects.all() # fetching all the catagory from the date base

    if q:
        products=Products.objects.filter(
            Q(catagory__name__icontains=q)
        )
    else:
        products=Products.objects.all() # fetching all the products from the database

    return render (request,'index.html',{'products':products,'catagories':catagories})

#about page

def about(request):

    return render(request,'about.html',{})
#user login
def login_user(request):
    #if it is a post method
    if request.method=="POST":
        username=request.POST['username'] #fetching the username from the submission
        password=request.POST['password'] #fetching the password from the submission

        #checking if the is valid using authenticate method
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user) #login in the user
            messages.success(request,"You are successfully logged in")
            return redirect('home')
        else:
            messages.error(request,{"some thing went wrong"})
            return redirect('login')


    #if it's not a post method
    else:
        return render(request,'login.html',{})


#user logout
def logout_user(request):
    logout(request) #logging out the user
    return redirect('login')

#user register

def register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            
            user=authenticate(request,username=username,password=password)
            #logging in
            login(request,user)
            messages.success(request,"Successfully registered")
            return redirect('home')
        else:
            messages.error(request,"something went wrong")
    else:
        form=SignUpForm()
    return render(request,'register.html',{'form':form})


#getting the products
def product(request,pk):
    product=Products.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

#getting the category


    