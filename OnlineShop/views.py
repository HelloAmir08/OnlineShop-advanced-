from django.shortcuts import render
from OnlineShop.models import Product


# Create your views here.

def homepage(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'OnlineShop/index.html', context)

def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render (request, 'OnlineShop/product_details.html', context)

def about(request):
    return render(request, 'OnlineShop/about.html')

def contact(request):
    return render(request, 'OnlineShop/contact.html')

def login(request):
    return render(request, 'OnlineShop/login.html')

def register(request):
    return render(request, 'OnlineShop/register.html')