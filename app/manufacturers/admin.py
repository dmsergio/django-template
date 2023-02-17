from django.contrib import admin

from manufacturers.models import Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )
