from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Article, News, ImageGallery

# Function Based Views
# Landing Page
def Landing(request):
    article = Article.objects.all()
    category = Category.objects.all()
    news = News.objects.all()
    return render(request, 'article/index.html')


# Class Based Views
# Article Read
class ArticleView(DeleteView):
    model = Article
    template_name = 'article/article.html'

# News Read
class NewsView(DetailView):
    model = News
    template_name = 'article/news.html'