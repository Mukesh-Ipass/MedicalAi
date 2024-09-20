from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
