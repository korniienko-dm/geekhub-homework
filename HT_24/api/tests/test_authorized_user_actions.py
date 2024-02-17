from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse
from django.core.serializers import serialize
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Category
from main.models import Product


class ProductAPITest(APITestCase):
    """
    Test cases for authorized user
    """

    def setUp(self):
        """Set up initial data for the tests."""
        self.user = CustomUser.objects.create_user(username='user', password='useruser')
        self.client.login(username='user', password='useruser')
        self.category = Category.objects.create(name='Test Category')
        self.product_data = {
            'name': 'Test Product',
            'brand': 'Test Brand',
            'product_id': 'p-SPM8792480723',
            'image': 'test_image.jpg',
            'price': '10.00',
            'seo_url': 'test_seo_url',
            'user_manual': 'test_manual',
            'pre_description': 'test_pre_description',
            'short_description': 'test_short_description',
            'long_description': 'test_long_description',
            'seller': 'Test Seller',
            'category': Category.objects.get(id=1),
            'parent_category': 'Test Category',
            'parent_category_url': 'test_parent_category_url'
        }
        self.product = Product.objects.create(**self.product_data)

    def tearDown(self):
        """Clean up after each test."""
        Category.objects.all().delete()
        Product.objects.all().delete()

    def test_list_products(self):
        """Test retrieving a list of products."""
        url = reverse('products_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        """Test creating a new product."""
        url = reverse('products_list')
        category = Category.objects.get(name=self.product_data['parent_category'])
        category_id = category.id
        self.product_data['category'] = category_id
        response = self.client.post(url, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_information_about_product(self):
        """Test retrieving information about a specific product."""
        url = reverse('product_details', kwargs={'pk': self.product.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        """Test updating an existing product."""
        url = reverse('product_details', kwargs={'pk': self.product.id})
        category = Category.objects.get(name=self.product_data['parent_category'])
        category_id = category.id
        product_data = self.product_data
        product_data['category'] = category_id
        product_data['name'] = "Updated Test Product"
        response = self.client.put(url, product_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_product(self):
        """Test deleting an existing product."""
        url = reverse('product_details', kwargs={'pk': self.product.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_product_to_cart(self):
        """Test adding a product to the shopping cart."""
        url = reverse('cart_list')
        data = {
            'product_id': self.product.id,
            'product_quantity': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_products_in_cart(self):
        """Test retrieving products in the shopping cart."""
        url = reverse('cart_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_product_quantity_in_cart(self):
        """Test changing the quantity of a product in the shopping cart."""
        url = reverse('cart_list')
        data = {
            'product_id': self.product.id,
            'product_quantity': 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data_list = [(item['product_id'], item['product_quantity']) for item in response.data]
        expected_data = [(self.product.id, 5)]
        self.assertEqual(response_data_list, expected_data)

    def test_delete_product_from_cart(self):
        """Test deleting a product from the shopping cart."""
        url = reverse('cart_list')
        product_id = self.product.id
        data = {'product_id': product_id}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cart_items_count = len(response.data)
        self.assertEqual(cart_items_count, 0)

    def test_list_categories(self):
        """Test retrieving a list of categories."""
        url = reverse('category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        """Test creating a new category."""
        url = reverse('category_list')
        data = {'name': 'New_category'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_category(self):
        """Test updating an existing category."""
        url = reverse('category_details', kwargs={'pk': self.category.id})
        updated_category_data = {'name': 'New Test Category'}
        response = self.client.put(url, updated_category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_category(self):
        """Test deleting an existing category."""
        url = reverse('category_details', kwargs={'pk': self.category.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
