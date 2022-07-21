from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone', 'otp')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('phone', 'otp')


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=10)
    otp  = forms.CharField(max_length=5)





