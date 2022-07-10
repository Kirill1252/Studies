from rest_framework import viewsets, permissions

from .serializers import PostSerializer
from blog.models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]