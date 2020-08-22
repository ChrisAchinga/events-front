from django.urls import path
from . import views
from .views import ArticleView, NewsView, contactView, successView

urlpatterns = [
    path('', views.Landing, name='home'),
    path('read/<int:pk>', ArticleView.as_view(), name='article'),
    path('news/<int:pk>', NewsView.as_view(), name='news'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
]
