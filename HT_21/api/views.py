from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .serializers import CategorySerializer
from .serializers import CartProductSerializer
from main.models import Category
from main.models import Product
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
        product_id = int(request.data.get("product_id", 0))
        product_quantity = int(request.data.get("product_quantity", 0))
        id_product_list = Product.objects.all()
        product_ids = list(id_product_list.values_list('id', flat=True))

        if not product_id in product_ids:
            return Response({"error": "Invalid product id"})

        cart_data = request.session.get(
            'product_data', {}).get('cart_list', [])
        product_data = {'product_id': str(
            product_id), 'product_quantity': str(product_quantity)}

        if not str(product_id) in [product['product_id'] for product in cart_data]:
            cart_data.append(product_data)
            id_products_in_cart = [elem['product_id'] for elem in cart_data]

            request.session['product_data'] = {'cart_list': cart_data}
            request.session['id_list'] = id_products_in_cart
            request.session.modified = True

            serializer = CartProductSerializer(data=cart_data, many=True)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
        return Response({"error": "Product ID already added to cart"})

    def put(self, request, *args, **kwargs):
        """PUT method for updating the quantity of a product in the shopping cart."""
        pk = kwargs.get("pk", None)
        product_id_to_update = str(pk)
        try:
            product_quantity = int(request.data.get("product_quantity", 0))
        except ValueError:
            return Response({"error": "Invalid product quantity"}, status=400)
        cart_data = request.session.get(
            'product_data', {}).get('cart_list', [])
        for item in cart_data:
            if item['product_id'] == product_id_to_update:
                item['product_quantity'] = product_quantity
                break
        request.session['product_data']['cart_list'] = cart_data
        request.session.modified = True

        serializer = CartProductSerializer(data=cart_data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """DELETE method for removing a product from the shopping cart."""
        pk = kwargs.get("pk", None)
        product_id_to_remove = str(pk)
        cart_data = request.session.get(
            'product_data', []).get('cart_list', [])
        id_products_in_cart = [elem['product_id'] for elem in cart_data]

        if not product_id_to_remove in id_products_in_cart:
            return Response({"error": "No such product in the store cart"}, status=400)

        updated_cart_data = [
            item for item in cart_data if item['product_id'] != product_id_to_remove]
        id_products_in_cart = [elem['product_id']
                               for elem in updated_cart_data]

        request.session['product_data']['cart_list'] = updated_cart_data
        request.session['id_list'] = id_products_in_cart
        request.session.modified = True

        serializer = CartProductSerializer(data=updated_cart_data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
