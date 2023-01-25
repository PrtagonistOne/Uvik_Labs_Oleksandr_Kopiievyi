from django import forms

from django.forms import ModelForm

from .models import Comment
from post.validation.custom_validation import validate_comment_content


class CommentForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'No swear words!'}))

    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        if validate_comment_content(content):
            raise forms.ValidationError("Error! Watch your mouth!")
        return content
