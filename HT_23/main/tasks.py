from .models import Product
from .models import Category
from app_sears_product.celery import app
from utils.parser import SearsProductScraping
from celery import shared_task


@app.task
def parse_and_save_product(product_id):
    """Parse and save product information."""
    scraper = SearsProductScraping(product_id)
    data = scraper.get_product_informations()
    parent_category_name = data.get('parent_category')
    category, category_created = Category.objects.get_or_create(name=parent_category_name)
    data['category'] = category
    product, product_created = Product.objects.get_or_create(product_id=product_id, defaults=data)


@app.task
def synchronization_product_info(product_id):
    """Updating product information from the Sears website"""
    product = Product.objects.get(id=product_id)
    scraper = SearsProductScraping(product.product_id)
    updated_data = scraper.get_product_informations()
    for key, value in updated_data.items():
        setattr(product, key, value)
    category_name = updated_data.get('parent_category')
    category, _ = Category.objects.get_or_create(name=category_name)
    product.category = category
    product.save()
