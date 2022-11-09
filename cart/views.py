from django.shortcuts import redirect, render
from cart.cart import Cart
from products.models import Product
# Create your views here.


def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product)
    
    return redirect("category", product.categories_id)


def delete(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.delete(product)
    return redirect("category", product.categories_id)

def subtract(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.subtract(product)
    return redirect("category", product.categories_id)
    


def clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("index")

def confirm(request):
    clear(request)
    return redirect("/?ok") 


    