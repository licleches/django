from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.StringRelatedField(source='category', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'category_name')