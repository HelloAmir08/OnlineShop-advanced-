from django.shortcuts import render, redirect
from OnlineShop.forms import CommentForm, OrderForm
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

    comment_form = CommentForm()
    order_form = OrderForm()

    if request.method == "POST":
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.product = product
                comment.save()
                return redirect('product_details', pk=pk)

        elif 'order_submit' in request.POST:
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                order = order_form.save(commit=False)
                order.product = product
                order.save()
                return redirect('product_details', pk=pk)

    context = {
        'product': product,
        'comments': comments,
        'order_form': order_form,
        'comment_form': comment_form
    }

    return render(request, 'OnlineShop/product_details.html', context)


"""
    old incorrect version 
"""
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.product = product
    #         comment.save()
    #         return redirect('product_details', pk=pk)
    # else:
    #     form = CommentForm()
    #
    # if request.method == 'POST':
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         order = form.save(commit=False)
    #         order.product = product
    #         order.save()
    #         return redirect('product_details', pk=pk)
    # else:
    #     form = OrderForm()

    # context = {
    #     'product': product,
    #     'comments': comments,
    #     'form': form
    # }
    # return render (request, 'OnlineShop/product_details.html', context)

def about(request):
    return render(request, 'OnlineShop/about.html')

def contact(request):
    return render(request, 'OnlineShop/contact.html')

def login(request):
    return render(request, 'OnlineShop/login.html')

def register(request):
    return render(request, 'OnlineShop/register.html')

