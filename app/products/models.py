from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel
from manufacturers.models import Manufacturer


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
    category = models.ForeignKey(
        to="ProductCategory",
        on_delete=models.SET_NULL,
        verbose_name=_("Category"),
        db_column="category_id",
        related_name="products",
        null=True,
        blank=True,
    )
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.SET_NULL,
        verbose_name=_("Manufacturer"),
        db_column="manufacturer_id",
        related_name="products",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "product"
        app_label = "products"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        constraints = [
            models.UniqueConstraint(
                fields=["sku"],
                name=_("%(app_label)s_%(class)s: sku must be unique!"),
            )
        ]

    def __str__(self) -> str:
        return f"[{self.sku}] {self.name}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.sku} ({self.pk})>"


class ProductCategory(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )

    class Meta:
        db_table = "product_category"
        app_label = "products"
        verbose_name = _("Product Category")
        verbose_name_plural = _("Products Categories")
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name=_("%(app_label)s_%(class)s: name must be unique!"),
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.name} ({self.pk})>"
