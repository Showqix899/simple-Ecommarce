from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Products
from django.http import JsonResponse

# Create your views here.


#for curt summary
def curt_summary(request):
    cart=Cart(request)
    cart_prods=cart.get_prods()
    return render (request,'curt_summary.html',{'cart_prods':cart_prods})

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

        #getting the length
        cart_quantity=cart.__len__()

        return JsonResponse({'qty':cart_quantity})

        #return response
        #@return JsonResponse({'Product name': product.id})


