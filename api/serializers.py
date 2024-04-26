from rest_framework import serializers
from api.models import ProductTable, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTable
        fields = "__all__"
