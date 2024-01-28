from django.urls import path
from . import views


urlpatterns = [
    path('cart/', views.show_cart_product, name='cart_page'),
    path('cart/swap_cart/', views.swap_cart, name='swap_cart'),
    path('send_quantity_products/', views.send_form_quantity_cart, name='send_form_quantity_cart'),
    path('clean_cart/', views.clean_cart, name='clean_cart'),
]
 