from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, required=True, initial='')
    email = forms.EmailField(max_length=255, required=True, initial='')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
