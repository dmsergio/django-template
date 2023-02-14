from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class BaseModel(TimeStampedModel):
    class Meta:
        abstract = True
