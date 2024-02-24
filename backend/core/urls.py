"""core URL Configuration

The `urlpatterns` list routes URLs to views.
For more information please see:
https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

admin.site.site_header = admin.site.site_title = "Django With Vue JS Blog"
admin.site.index_title = "bienvenu sur votre tableau d'administration".capitalize()

urlpatterns = [
    path('api/v1/', include('blog.urls', namespace='blog')),

    path('summernote/', include('django_summernote.urls')),
    path(settings.ADMIN_URL, admin.site.urls),

    path('api-auth', include('rest_framework.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
