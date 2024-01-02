from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product
from .forms import ProductForm
from utils.parser import SearsProductScraping
from concurrent.futures import ThreadPoolExecutor


def index(requests):
    """Render the home page."""
    products = Product.objects.all()
    return render(requests, 'main/index.html', {'products': products})

def show_all_products(requests):
    """Render a page showing all products."""
    products = Product.objects.all()
    return render(requests, 'main/show_all_products.html', {'products': products})

def product_details(request, product_id):
    """Render the details page for a specific product."""
    products = Product.objects.all()
    product_id = Product.objects.get(id=product_id)
    return render(request, 'main/product_details.html', {'product_id': product_id, 'products': products})

def add_products(request):
    """Render the page for adding new products or process the form submission."""
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_ids = form.cleaned_data['product_ids']
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(parse_and_save_product, product_id) for product_id in product_ids]
                for future in futures:
                    future.result()
            return redirect('show_products')
    else:
        form = ProductForm()
    return render(request, 'main/add_products.html', {'form': form, 'products': products})

def parse_and_save_product(product_id):
    """Parse and save product information."""
    scraper = SearsProductScraping(product_id)
    data = scraper.get_product_informations()
    Product.objects.create(**data)
