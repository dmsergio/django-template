from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "sku",
        "name",
        "type",
    )
    fields = (
        ("sku", "name"),
        "type",
    )
    search_fields = (
        "sku",
        "name",
    )
