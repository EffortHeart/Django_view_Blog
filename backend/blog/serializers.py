# blog.serializers.py

from rest_framework import serializers

from blog.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'uuid', 'name', 'image', 'slug'
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'uuid', 'category', 'name',
            'subtitle', 'body', 'image',
            'status', 'published', 'slug'
        )
