from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('user', 'post_text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('user', 'comment_text')
