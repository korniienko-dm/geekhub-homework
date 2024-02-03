from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.decorators.http import require_POST
from concurrent.futures import ThreadPoolExecutor
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.http import JsonResponse
from utils.parser import SearsProductScraping
from utils.logger import logger
from .view_service.cart_manage import CartManageProduct
from .models import Product
from .models import Category
from .forms import ProductForm
from .forms import ProductUpdateForm


def index(request):
    """Render the home page."""
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})


def show_all_products(request):
    """Render a page showing all products."""
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products,
               'categories': categories,}
    return render(request, 'main/show_all_products.html', context)


def show_products_in_category(request, category_name):
    """Render the page displaying products in a specific category."""
    products = Product.objects.all()
    context = {'category_name': category_name,
               'products': products,}
    return render(request, 'main/show_products_in_category.html', context)


def product_details(request, product_id):
    """Render the details page for a specific product."""
    products = Product.objects.all()
    product = Product.objects.get(id=product_id)
    return render(request,
                  'main/product_details.html',
                  {'product': product,
                  'products': products,})


def is_superuser(user):
    """ Check if the user has superuser privileges."""
    return user.is_superuser


class ProductUpdate(UserPassesTestMixin, UpdateView):
    """View for updating product information with superuser permissions."""
    model = Product
    form_class = ProductUpdateForm
    template_name = 'main/update_product.html'
    text_error = 'You do not have permission to update this product.'
    def get_success_url(self):
        """Returns the URL to redirect to after a successful update."""
        return self.object.get_absolute_url()
    def test_func(self):
        """Checks if the user has superuser permissions."""
        return self.request.user.is_superuser
    def handle_no_permission(self):
        """Handles the case where the user lacks superuser permissions."""
        messages.error(self.request, self.text_error)
        return redirect('home')


class ProductDelete(UserPassesTestMixin, DeleteView):
    """View for deleting a product with superuser permissions."""
    model = Product
    template_name = 'main/delete_product.html'
    success_url = '/show_all_products'
    text_error = 'You do not have permission to delete this product.'
    def test_func(self):
        """Checks if the user has superuser permissions."""
        return self.request.user.is_superuser
    def handle_no_permission(self):
        """Handles the case where the user lacks superuser permissions."""
        messages.error(self.request, self.text_error)
        return redirect('home')


@user_passes_test(is_superuser, login_url='home')
def add_products(request):
    """Render the page for adding new products or process the form submission."""
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_ids = form.cleaned_data['product_ids']
            try:
                with ThreadPoolExecutor() as executor:
                    futures = [executor.submit(
                        parse_and_save_product, product_id) for product_id in product_ids]
                    for future in futures:
                        future.result()
            except Exception as error:
                logger.error(f"Error in operation: {error}", exc_info=True)
            finally:
                return redirect('show_products')
    else:
        form = ProductForm()
    return render(request, 'main/add_products.html', {'form': form, 'products': products})


def sync_product_info(request, pk, product_id_sears):
    """Update product information by syncing with an external source."""
    product_id_db = pk
    product_id_sears = product_id_sears
    product = get_object_or_404(Product, product_id=product_id_sears)
    scraper = SearsProductScraping(product_id_sears)
    updated_data = scraper.get_product_informations()
    for key, value in updated_data.items():
        setattr(product, key, value)
    product.save()
    return redirect('product_update', pk=product_id_db)


def parse_and_save_product(product_id):
    """Parse and save product information."""
    scraper = SearsProductScraping(product_id)
    data = scraper.get_product_informations()
    parent_category_name = data.get('parent_category')
    category, category_created = Category.objects.get_or_create(name=parent_category_name)
    data['category'] = category
    product, product_created = Product.objects.get_or_create(product_id=product_id, defaults=data)


def swap_product_in_cart(request):
    """Add or remove a product from the shopping cart in the session."""
    cart_manage = CartManageProduct(request=request)
    cart_list = cart_manage.get_cart_list()
    updated_cart_list = cart_manage.update_cart_list(cart_list)
    cart_manage.update_session(updated_cart_list)
    return redirect('show_products')


def get_cart_count(request):
    """Get the number of items in the cart"""
    count = len(request.session.get('product_data', {}).get('cart_list', []))
    return JsonResponse({'count': count})


def get_product_price(request, product_id):
    """Get the price of a product."""
    cart_list = request.session.get('product_data', {}).get('cart_list', [])
    for product in cart_list:
        if product['product_id'] == str(product_id):
            return JsonResponse({'price': product.get('price', '')})
    return JsonResponse({'price': ''})
