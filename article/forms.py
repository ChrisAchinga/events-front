from django import forms
from .models import Post, Category

# choices = Category.objects.all().values_list('name', 'name')


def widget_attrs(placeholder=''):
    return {'class': 'form-control', 'placeholder': placeholder}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs=widget_attrs('Enter title')),
            'title_tag': forms.TextInput(attrs=widget_attrs()),
            'author': forms.Select(attrs=widget_attrs()),
            'body': forms.Textarea(attrs=widget_attrs())
            # 'category': forms.Select(attrs=widget_attrs(), choices=choices),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs=widget_attrs('Enter title')),
            'body': forms.Textarea(attrs=widget_attrs())
        }
