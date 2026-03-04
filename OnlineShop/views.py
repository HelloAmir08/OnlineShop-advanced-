from django.shortcuts import render, redirect

from OnlineShop.forms import CommentForm
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
    comments = product.comments.order_by('-id')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_details', pk=pk)
    else:
        form = CommentForm()

    context = {
        'product': product,
        'comments': comments,
        'form': form
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

