# blog.models.py

from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.crypto import get_random_string

from common.utilitary import img_url
from blog.managers import PostManager
from common.models import BaseTimeStampModel, UUIDSlugMixin


NULL_AND_BLANK = {'null': True, 'blank': True}


class Category(UUIDSlugMixin, BaseTimeStampModel):
    
    name = models.CharField(
        unique=True,
        max_length=120,
        default="Non définie",
        verbose_name="type de catégorie d'article",
        help_text="Définir le type de catégorie de l'article.",
        **NULL_AND_BLANK
    )
    image = models.ImageField(
        upload_to=img_url,
        verbose_name="ajouter une image",
        help_text="ajouter une image descriptive de l'article.",
        **NULL_AND_BLANK
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'catégories'
        indexes = [models.Index(fields=['uuid'])]

    def __str__(self):
        return self.name

    @admin.display(description="catégorie")
    def category_name(self):
        return self.name

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{get_random_string(6)}".lower()
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def posts(self):
        return Post.objects.filter(category=self)

    @admin.display(description="nombre d'articles dans cette catégorie")
    def post_count(self):
        return self.posts().count()


class Post(UUIDSlugMixin, BaseTimeStampModel):
    
    P = 'Publié'
    B = 'Brouillon'
    R = 'Relecture'

    STATUS_CHOICES = (
        (P, 'Publié'),
        (B, 'Brouillon'),
        (R, 'Relecture')
    )

    file_prepend = "post/image/"
    
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        verbose_name="catégorie",
        **NULL_AND_BLANK
    )
    name = models.CharField(
        unique=True,
        max_length=255,
    	verbose_name="titre de l'article",
    	help_text="Définir le titre de l'article."
    )
    subtitle = models.CharField(
        max_length=255,
    	verbose_name="sous-titre",
    	help_text="Définir un sous-titre de l'article.",
        **NULL_AND_BLANK
    )
    body = models.TextField(
        verbose_name="Contenu de l'article",
        help_text="Éditer le contenu de l'article."
    )
    image = models.ImageField(
        upload_to=img_url,
        verbose_name="ajouter une image",
        help_text="ajouter une image descriptive de l'article.",
        **NULL_AND_BLANK
    )
    view = models.PositiveIntegerField(
        default=0,
        editable=False,
        verbose_name="nombre de vues"
    )
    status = models.CharField(
        default=B,
        max_length=10,
    	verbose_name="status",
    	choices=STATUS_CHOICES,
        help_text="définir le status de l'article."
    )
    published = models.DateTimeField(
        auto_now_add=False, auto_now=False,
        verbose_name='date et de publication',
        help_text="Programmé la date et l'heure de publication"
    )

    objects = PostManager()

    class Meta:
        ordering = ['-published']
        get_latest_by = ['-published']
        verbose_name_plural = 'articles'
        indexes = [models.Index(fields=['uuid'])]
    
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{get_random_string(6)}".lower()
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


@receiver([models.signals.pre_save], sender=Post)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        try:
            old_image = Post.objects.get(pk=instance.pk).image
            if old_image and old_image.url != instance.image.url:
                old_image.delete(save=False)
        except: pass
