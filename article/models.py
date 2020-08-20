from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    # list of required categories required
    CATEGORY_LIST = (
        ('beauty', 'Beauty'),
        ('trends', 'Trends'),
        ('travel', 'Travel'),
        ('fashion', 'Fashion'),
        ('culture', 'Culture'),
        ('food', 'Food'),
        ('entrepreneur', 'Entrepreneur'),
        ('fashion-pictorial', 'Fashion Pictorial'),
        ('health', 'Health'),
        ('men', 'Mens Corner'),
        ('lifestyle', 'Lifestyle'),
        ('general', 'General')
    )
    name = models.CharField('Category Name', choices=CATEGORY_LIST, default='general', max_length=20)
    description = models.TextField(max_length=250, null=False)
    image = models.ImageField(upload_to='uploads/', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Article(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=False)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')