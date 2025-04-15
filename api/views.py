from rest_framework import generics
from .serializers import CommentSerializer
from blog.models import Comment

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
