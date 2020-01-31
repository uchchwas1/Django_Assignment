from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product


# Create your views here.

def index(request):
    product_name= request.POST["product_name"]
    decs = request.POST["decs"]
    image= request.POST["image"]  
    product_info = Product(product_name= product_name, decs= decs, image= image)
    product_info.save()
    return render(request, 'insertData/insertData.html')

