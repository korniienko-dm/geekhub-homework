from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add_products', views.add_products, name='add_products'),
    path('show_all_products', views.show_all_products, name='show_products'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    path('swap_product_in_cart', views.swap_product_in_cart, name='swap_product_in_cart'),
    path('product_details/<int:pk>/update', views.ProductUpdate.as_view(), name='product_update'),
    path('product_details/<int:pk>/delete', views.ProductDelete.as_view(), name='product_delete'),
    path('product_details/<int:pk>/<str:product_id_sears>/sync_product_info', views.sync_product_info, name='sync_product_info'),
    path('category/<str:category_name>', views.show_products_in_category, name='show_products_in_category'),
]
