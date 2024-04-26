from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.models import ProductTable, Category
from api.serializers import CategorySerializer, ProductSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        AllowAny,
    ]
    lookup_field = "Name"


class ProductViewset(viewsets.ModelViewSet):
    queryset = ProductTable.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        AllowAny,
    ]
    lookup_field = "product_name"
