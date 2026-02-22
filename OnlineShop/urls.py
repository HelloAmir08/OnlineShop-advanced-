from django.urls import path
from OnlineShop import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('product_details/<int:pk>/', views.product_details, name='product_details'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
