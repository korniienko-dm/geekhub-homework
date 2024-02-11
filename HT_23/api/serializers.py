import logging
from rest_framework import serializers
from main.models import Category
from main.models import Product
from utils.parser import SearsProductScraping
from main.tasks import synchronization_product_info


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'brand',
            'product_id',
            'image',
            'price',
            'seo_url',
            'user_manual',
            'pre_description',
            'short_description',
            'long_description',
            'seller',
            'category',
            'parent_category',
            'parent_category_url',
        )

    def create(self, validated_data):
        instance = super().create(validated_data)
        synchronization_product_info.apply_async(args=[instance.id])
        return instance


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class CartProductSerializer(serializers.Serializer):
    """
    Serializer for cart product data.
    """
    product_id = serializers.IntegerField()
    product_quantity = serializers.IntegerField()
