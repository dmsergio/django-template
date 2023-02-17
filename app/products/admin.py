from django.contrib import admin

from products.models import Product
from products.models import ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "sku",
        "name",
        "type",
        "category",
    )
    fields = (
        ("sku", "name"),
        "type",
        "category",
    )
    search_fields = (
        "sku",
        "name",
    )


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    fields = (
        "name",
    )
