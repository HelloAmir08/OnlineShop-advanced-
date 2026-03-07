from django.urls import path
from cart.views import cart_view, add_to_cart_view
urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<int:product_id>/', add_to_cart_view, name='add_to_cart'),
]