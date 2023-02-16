from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class ProductTypeChoices(models.TextChoices):
    PRODUCT = ("product", _("Product"))
    CONSUMABLE = ("consumable", _("Consumable"))
    SERVICE = ("service", _("Service"))


class Product(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    sku = models.CharField(
        max_length=50,
        verbose_name=_("SKU"),
    )
    type = models.CharField(
        max_length=50,
        verbose_name=_("Type"),
        choices=ProductTypeChoices.choices,
        default=ProductTypeChoices.PRODUCT,
    )

    class Meta:
        db_table = "product"
        app_label = "products"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name=_("%(app_label)s_%(class)s: name must be unique!"),
            )
        ]

    def __str__(self) -> str:
        return f"[{self.sku}] {self.name}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.sku} ({self.pk})>"
