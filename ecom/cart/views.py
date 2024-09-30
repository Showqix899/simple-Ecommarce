from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Products
from django.http import JsonResponse

# Create your views here.


#for curt summary
def curt_summary(request):
    return render (request,'curt_summary.html',{})

def cart_add(request):
    #get the cart
    cart=Cart(request)
    #test for Post
    if request.POST.get('action')=='post':
        #get the product id
        product_id=int(request.POST.get('product_id'))

        #get the product from the Product data model
        product=get_object_or_404(Products,id=product_id)

        #save the session
        cart.add(product=product)

        #return response
        return JsonResponse({'Product name': product.id})


