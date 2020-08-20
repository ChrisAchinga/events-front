from django.urls import path
# from . import views
from .views import homeView, detailView, AddPost, UpdatePost, DeletePost, AddCategory, CategoryView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', homeView.as_view(), name='home'),
    path('article/<int:pk>', detailView.as_view(), name='article-detail'),
    path('add/', AddPost.as_view(), name='add'),
    path('add-category/', AddCategory.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name='update'),
    path('article/del/<int:pk>', DeletePost.as_view(), name='delete'),
    path('category/<str:cats>/', CategoryView, name='category')
]
