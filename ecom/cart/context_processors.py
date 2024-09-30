from .cart import Cart

#create a context processor so that cart can work in all the page

def cart(request):
    #return the default data from our cart
    return {'cart':Cart(request)} 