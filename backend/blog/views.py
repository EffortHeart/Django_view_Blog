# blog.views.py

from django.shortcuts import get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Post, Category
from blog.serializers import CategorySerializer, PostSerializer


class CategoryListView(APIView):

    def get(self, request, *args, **kwargs):
        categorie = Category.objects.all()
        post_in_categorie = Post.objects.filter(category=categorie).published()[:10]
        serializer = CategorySerializer(categorie)
        return Response(serializer.data)


category_detail_view = CategoryListView.as_view() 


class PostListView(APIView):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.published()[:10]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


post_list_view = PostListView.as_view() 


class PostDetailView(APIView):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)


post_detail_view = PostDetailView.as_view()
