# common.models.py

import uuid

from django.db import models
from django.contrib import admin
from django.utils import timezone


NULL_AND_BLANK = {
    'null': True,
    'blank': True
}

class BaseTimeStampModel(models.Model):
    
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDSlugMixin(models.Model):

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid'
    )
    slug = models.SlugField(
        unique=True,
        editable=False,
        verbose_name='slug',
        unique_for_date='created_at',
        help_text='Automatiquement formé à partir du nom.',
        **NULL_AND_BLANK
    )

    class Meta:
        abstract = True
