from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from products.models import Product
from products.models import ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "sku",
        "name",
        "type",
        "category_link",
        "manufacturer_link",
    )
    fields = (
        ("sku", "name"),
        "type",
        "category",
        "manufacturer",
    )
    search_fields = (
        "sku",
        "name",
    )

    def category_link(self, obj):
        if obj.category:
            url = reverse(
                f"admin:products_productcategory_change",
                args=[obj.category.pk],
            )
            return format_html('<a href="{}">{}</a>', url, str(obj.category))

    category_link.short_description = "Category"

    def manufacturer_link(self, obj):
        if obj.manufacturer:
            url = reverse(
                f"admin:manufacturers_manufacturer_change",
                args=[obj.manufacturer.pk],
            )
            return format_html('<a href="{}">{}</a>', url, str(obj.manufacturer))

    manufacturer_link.short_description = "Manufacturer"



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
    fields = (
        "name",
    )
