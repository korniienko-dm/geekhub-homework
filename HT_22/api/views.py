from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .serializers import CategorySerializer
from .serializers import CartProductSerializer
from main.models import Category
from main.models import Product
from main.view_service.cart_manage import CartManageProduct
from .permission import IsAdminOrReadOnly
from .permission import IsAuthenticatedOrReadOnly


class ProductAPIList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CategoryAPIList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )


class CategoryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, and deleting a specific category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )


class CartAPIView(APIView):
    """
    API endpoint for managing the shopping cart.

    Allowed HTTP Methods:
        - GET: Retrieve the contents of the shopping cart.
        - POST: Add a product to the shopping cart.
        - PUT: Update the quantity of a product in the shopping cart.
        - DELETE: Remove a product from the shopping cart.

    Permissions:
        - Authenticated users can perform any action.
        - Read-only for unauthenticated users.
    """

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        """GET method for retrieving the contents of the shopping cart."""
        try:
            cart_data = request.session.get(
                'product_data', []).get('cart_list', [])
            serializer = CartProductSerializer(data=cart_data, many=True)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
        except:
            return Response({"error": "Products in cart does not exists"})

    def post(self, request, *args, **kwargs):
        """ POST method for adding a product to the shopping cart."""
        id_product_list = Product.objects.all()
        product_ids = list(id_product_list.values_list('id', flat=True))
        product_id = request.data.get('product_id')

        if not product_id in product_ids:
            return Response({"error": "Invalid product id"})

        product_id = str(product_id)
        product_quantity = request.data.get('product_quantity')
        cart_manage = CartManageProduct(
            request=request,
            product_id=product_id,
            product_quantity=product_quantity
        )
        cart_list = cart_manage.get_cart_list()
        update_cart_list = cart_manage.update_cart_list(cart_list=cart_list)
        cart_manage.update_session(update_cart_list)

        serializer = CartProductSerializer(data=cart_list, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        """PUT method for updating the quantity of a product in the shopping cart."""
        product_id = str(request.data.get('product_id'))
        product_quantity = request.data.get('product_quantity')

        cart_manage = CartManageProduct(
            request=request,
            product_id=product_id,
            product_quantity=product_quantity
        )
        cart_list = cart_manage.get_cart_list()
        update_cart_list = cart_manage.update_product_quantity(cart_list=cart_list)
        cart_manage.update_session(update_cart_list)

        serializer = CartProductSerializer(data=cart_list, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """DELETE method for removing a product from the shopping cart."""
        product_id_delete = str(request.data.get('product_id'))

        cart_manage = CartManageProduct(
            request=request,
            product_id=product_id_delete,
        )
        cart_list = cart_manage.get_cart_list()
        update_cart_list = cart_manage.delete_product_from_cart(cart_list=cart_list)
        cart_manage.update_session(update_cart_list)

        serializer = CartProductSerializer(data=update_cart_list, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
