from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    author = models.CharField(max_length=100)
    body = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.article.title}"
