"""Generic abstract models for applications.

These are generic abstract models that will be used for multiple applications
at the same time. Please be aware that any changes to this abstract models
*won't* be catched by the migration system, due to the fact that they don't
belong to any specific app.
"""

from datetime import datetime
from django.db import models


class BaseFields(models.Model):
    """Base fields that should be included in all models."""

    active = models.BooleanField(default=True)
    date_modified = models.DateTimeField(blank=True, null=True, auto_now=True)
    date_created = models.DateTimeField(blank=True, null=True,
                                        default=datetime.now(), editable=False)

    class Meta:
        abstract = True
