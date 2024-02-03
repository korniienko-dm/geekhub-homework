from django.urls import path
from django.urls import include
from .views import ProductAPIList
from .views import ProductAPIDetailView
from .views import CategoryAPIList
from .views import CategoryAPIDetailView
from .views import CartAPIView


urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    path('api/v1/productlist/', ProductAPIList.as_view()),
    path('api/v1/productlist/<int:pk>/', ProductAPIDetailView.as_view()),

    path('api/v1/categorylist/', CategoryAPIList.as_view()),
    path('api/v1/categorylist/<int:pk>/', CategoryAPIDetailView.as_view()),

    path('api/v1/cartlist/', CartAPIView.as_view()),
    path('api/v1/cartlist/<int:pk>/', CartAPIView.as_view()),
    # path('api/v1/cartlist/<int:pk>/', CartAPIView.as_view()),
]
