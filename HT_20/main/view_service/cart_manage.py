"""
Shopping Cart Management Module

This module provides a class:
    - CartManageProduct, for managing product data in the shopping cart
      stored in the Django session.
"""

class CartManageProduct():
    """
    Manage product data in the shopping cart stored in the session.
    This class provides methods to retrieve, update, and manage product data
    in the shopping cart stored in the Django session.
    """

    def __init__(self, request):
        """Initialize the CartManageProduct object."""
        self.request = request

    def get_product_id(self):
        """Get product id from the session."""
        product_id = self.request.GET.get('product_id')
        return product_id

    def get_product_data(self):
        """Get product data, including product ID and quantity (default 1)."""
        product_id = self.get_product_id()
        product_data = {'product_id': product_id, 'product_quantity': 1}
        return product_data

    def get_cart_list(self):
        """Get cart list data from the session."""
        request = self.request
        product_data = request.session.get('product_data', {}).get('cart_list', [])
        return product_data

    def update_cart_list(self, cart_list):
        """Update the cart list based on the product ID."""
        product_id = self.get_product_id()
        product_data = self.get_product_data()
        if product_id in [item['product_id'] for item in cart_list]:
            return [item for item in cart_list if item['product_id'] != product_id]
        cart_list.append(product_data)
        return cart_list

    def update_session(self, cart_list):
        """Update the session with the modified cart list."""
        product_in_cart = [elem['product_id'] for elem in cart_list]
        self.request.session['product_data'] = {'cart_list': cart_list}
        self.request.session['id_list'] = product_in_cart
        self.request.session.modified = True
