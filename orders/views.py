from django.shortcuts import render

from cart.views import Cart, ProductCartUser

# Create your views here.

def new_order(request):
    cart = ProductCartUser(request)