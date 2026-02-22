from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'OnlineShop/home.html')

def product_details(request):
    return render (request, 'OnlineSHop/detail.html')