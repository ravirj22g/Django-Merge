from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','category','tag','thumbnail_image','featured_image',)


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone',
                  'city', 'state', 'country', 'about', 'designation',)