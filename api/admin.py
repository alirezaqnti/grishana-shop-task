from django.contrib import admin
from api.models import Category, ProductTable


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin View for Category"""

    pass


@admin.register(ProductTable)
class ProductTableAdmin(admin.ModelAdmin):
    pass
