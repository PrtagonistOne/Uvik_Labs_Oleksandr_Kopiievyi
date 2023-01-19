from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password_hash = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
