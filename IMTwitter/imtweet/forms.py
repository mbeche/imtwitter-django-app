from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):

    post_text = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':35}), label='')
    class Meta:
        model = Post
        fields = ('post_text',)

class CommentForm(forms.ModelForm):

    comment_text = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':35}), label='')
    class Meta:
        model = Comment
        fields = ('comment_text',)
