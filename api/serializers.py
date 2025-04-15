from rest_framework import serializers
from blog.models import Comment, Article

class CommentSerializer(serializers.ModelSerializer):
    article_title = serializers.CharField(source='article.title', read_only=True)
    article_id = serializers.IntegerField(source='article.id', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'name', 'text', 'created_at', 'article_title', 'article_id']
