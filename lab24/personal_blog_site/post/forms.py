from django import forms

from django.forms import ModelForm
from .models import Post, Comment
from post.validation.custom_validation import validate_comment_content


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['blog', 'title', 'content']
        exclude = ['username']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        if validate_comment_content(content):
            raise forms.ValidationError("Error! Watch your mouth!")
        return content
