
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

from django.forms import ModelForm, TextInput, Textarea, Select, CharField
from .models import *
from taggit.models import Tag

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded',
            'required': '',
            'name': 'name',
            'id': 'name',
            'type': 'text',
            'placeholder': '',
            'minlength': '1'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded',
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': '',
            'minlength': '8'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded pswdChecker',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': '',
            'minlength': '8'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'uk-input uk-border uk-border-rounded pswdChecker',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': '',
            'minlength': '8'
        })

    first_name = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')