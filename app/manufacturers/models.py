from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class Manufacturer(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )

    class Meta:
        db_table = "manufacturer"
        app_label = "manufacturers"
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")
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
