
from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product 
        fields = (
            "id",
            "category",
            "name", 
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "energy_values",
            "fatty_substances",
            "carbs",
            "proteins",
        ) 

class ProductSerializerAdd(serializers.ModelSerializer):
    class Meta: 
        model = Product 
        fields = (
            "id",
            "category",
            "name", 
            "description",
            "price",
        ) 


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products"
        )