from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from manufacturers.models import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "products_link",
    )

    def products_link(self, obj):
        count = obj.products.count()
        url = (
            reverse(f"admin:products_product_changelist")
            + "?"
            + urlencode({"manufacturer__pk": f"{obj.pk}"})
        )
        return format_html('<a href="{}">{} products</a>', url, count)

    products_link.short_description = "Products"
