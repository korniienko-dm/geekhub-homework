from django.urls import path
from django.urls import include
from .views import ProductAPIList
from .views import ProductAPIDetailView
from .views import CategoryAPIList
from .views import CategoryAPIDetailView
from .views import CartAPIView


urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    path('api/v1/productlist/', ProductAPIList.as_view(), name='products_list'),
    path('api/v1/productlist/<int:pk>/', ProductAPIDetailView.as_view(), name='product_details'),

    path('api/v1/categorylist/', CategoryAPIList.as_view(), name='category_list'),
    path('api/v1/categorylist/<int:pk>/', CategoryAPIDetailView.as_view(), name='category_details'),

    path('api/v1/cartlist/', CartAPIView.as_view(), name='cart_list'),
    path('api/v1/cartlist/<int:pk>/', CartAPIView.as_view(), name='cart_details'),
]
