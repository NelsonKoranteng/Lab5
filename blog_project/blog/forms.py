from django import forms
from .models import BlogPost
from .models import Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Ensure 'content' matches the field name in the `Comment` model