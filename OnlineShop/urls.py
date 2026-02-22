from django.urls import path
from OnlineShop import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('product_details/', views.product_details, name='product_details'),
]
