from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'avatar', 'draft', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username:')
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=16, min_length=3)
    password = forms.CharField(max_length=16, min_length=3)