from django.shortcuts import render
from django.shortcuts import redirect
from main.models import Product
from django.contrib.auth.decorators import user_passes_test


def is_user_authenticated(user):
    return user.is_authenticated


@user_passes_test(is_user_authenticated, login_url='home')
def show_cart_product(request):
    """Render the cart page with a list of all products."""
    products = Product.objects.all()
    return render(request, 'cart/cart.html', {'products': products})


def swap_cart(request):
    """Add or remove a product from the shopping cart in the session."""
    product_id = request.GET.get('product_id')
    product_data = {'product_id': product_id, 'product_quantity': 1}
    if product_id:
        cart_list = request.session.get(
            'product_data', {}).get('cart_list', [])
        if product_id in [item['product_id'] for item in cart_list]:
            cart_list = [
                item for item in cart_list if item['product_id'] != product_id]
        else:
            cart_list.append(product_data)
        product_in_cart = [elem['product_id'] for elem in cart_list]
        request.session['product_data'] = {'cart_list': cart_list}
        request.session['id_list'] = product_in_cart
        request.session.modified = True
    return redirect('cart_page')


def send_form_quantity_cart(request):
    """Update the quantity and total price of a product in the shopping cart."""
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('product_id')
        price = request.POST.get('price')
        calculate_total_price = float(price) * int(quantity)
        total_price = round(calculate_total_price, 2)
        cart_list = request.session.get(
            'product_data', {}).get('cart_list', [])
        for product in cart_list:
            if product['product_id'] == product_id:
                product['product_quantity'] = quantity
                product['price'] = str(total_price)
    request.session.modified = True
    return redirect('cart_page')


def clean_cart(request):
    """Clear the entire shopping cart in the session."""
    cart_list = request.session.get('product_data', {}).get('cart_list', [])
    product_in_cart = request.session['id_list']
    product_in_cart.clear()
    cart_list.clear()
    request.session.modified = True
    return redirect('cart_page')
