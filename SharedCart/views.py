from django.shortcuts import render
from .models import Product
 # Create your views here.

def index(request):
	products=Product.objects.all()
	return render(request,"cart.html",{'product':products})

def checkout(request):
    return render(request,"checkout.html")	