from rest_framework import serializers

from blog.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

