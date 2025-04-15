from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Article, Comment
from .forms import CommentForm

def index(request):
    articles = Article.objects.order_by('-publication_date')
    return render(request, 'blog/index.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all().order_by('-created_at')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(article=article, name=form.cleaned_data['name'], text=form.cleaned_data['text'])
            comment.save()
            return HttpResponseRedirect(reverse('article_detail', args=[pk]))
    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments, 'form': form})
