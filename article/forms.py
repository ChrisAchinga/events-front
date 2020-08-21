from django import forms
from .models import Category, Article, News, ImageGallery

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'cover_image', 'author', 'category', 'body_image', 'description', 'subheading', 'body', 'subheading1', 'body1')

        widgets = {
            'title': forms.TextInput(),
            'cover_image': forms.ImageField(),
            'author': forms.Select(),
            'category': forms.Select(),
            'body_image': forms.ImageField(),
            'subheading': forms.TextImput(),
            'body': forms.Textarea(),
            'subheading1': forms.TextImput(),
            'body1': forms.Textarea()
        }


class EditArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'cover_image', 'category', 'body_image', 'description', 'subheading', 'body', 'subheading1', 'body1')

        widgets = {
            'title': forms.TextInput(),
            'cover_image': forms.ImageField(),
            'category': forms.Select(),
            'body_image': forms.ImageField(),
            'subheading': forms.TextImput(),
            'body': forms.Textarea(),
            'subheading1': forms.TextImput(),
            'body1': forms.Textarea()
        }