from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, logout, authenticate

from .forms import LoginForm, RegisterForm
# Create your views here.


def home_view(request: HttpRequest):
    return render(request, "blog/index.html", )


def login_view(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            print(form.errors)  # Debugging: Check if errors exist
    else:
        form = LoginForm()
    return render(request, "blog/login.html", {"form": form})


def register_view(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("home")
