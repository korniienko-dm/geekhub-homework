from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Model representing a product category."""
    name = models.CharField('Category name', max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model representing a product."""
    name = models.CharField('Product name', max_length=250)
    brand = models.CharField('Brand name', max_length=250)
    product_id = models.CharField('Product ID', max_length=250)
    image = models.CharField('Image URL', max_length=250)
    price = models.CharField('Product price', max_length=250)
    seo_url = models.CharField('Product URL', max_length=250)
    user_manual = models.CharField('User manual', max_length=250)
    pre_description = models.TextField('Pre description')
    short_description = models.TextField('Short description')
    long_description = models.TextField('Long description')
    seller = models.CharField('Product seller', max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    parent_category = models.CharField('Parent category', max_length=250)
    parent_category_url = models.CharField('Parent category URL', max_length=250)

    def get_absolute_url(self):
        return reverse('product_details', args=[str(self.id)])

    def __str__(self):
        return self.name
