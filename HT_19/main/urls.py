from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add_products', views.add_products, name='add_products'),
    path('show_all_products', views.show_all_products, name='show_products'),
    path('product_details/<int:product_id>/',
         views.product_details, name='product_details'),
    path('swap_product_in_cart', views.swap_product_in_cart,
         name='swap_product_in_cart'),
]
