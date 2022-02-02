from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "get_absolute_url",
            "ordered_number"
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "products",
            "get_absolute_url",
        )
