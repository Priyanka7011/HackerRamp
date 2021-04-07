from django.shortcuts import render

# Create your views here.
def start(request):
	return render(request,"home.html")

def shirt(request):
	return render(request,"shirt.html")

def pant(request):
    return render(request,"pant.html")	