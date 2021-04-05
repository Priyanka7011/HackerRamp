from django.shortcuts import render
from SharedCart.models import Product
# Create your views here.


def index(request):
	return render(request,"index.html",{})


def room(request, room_name):
	products=Product.objects.all()
	return render(request, 'chatroom.html',{'room_name':room_name, 'product':products})
    
def checkout(request,room_name):
    return render(request,'checkout.html',{'room_name':room_name})    