# blog.managers.py

from django.db import models
from django.db.models import Q
from django.utils import timezone


class PostQuerySet(models.QuerySet):
    
    def published(self):
        return self.filter(
            status='Publié',
            published__lte=timezone.now()
        )

    def search(self, query):
        lookup = (
            Q(name__icontains=query)
            | Q(subtitle__icontains=query)
            | Q(body__icontains=query)
        )
        return self.filter(lookup).distinct()


class PostManager(models.Manager):
    
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)
