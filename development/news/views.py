from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from news.models import Post
from news.serializers import PostSerializer


class PostView(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
