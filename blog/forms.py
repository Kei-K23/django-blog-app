from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter your password"}
        )
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"})
    )
    email = forms.CharField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email", "type": "email"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password", "type": "password"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your confirm password", "type": "password"})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
