from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import login, logout

from .forms import AuthenticationFormWithStyle
# Create your views here.


def home_view(request: HttpRequest):
    return render(request, "blog/index.html", )


def login_view(request: HttpRequest):
    if request.method == "POST":
        form = AuthenticationFormWithStyle(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(user)
            return redirect('home')
    else:
        form = AuthenticationFormWithStyle()
    return render(request, "blog/login.html", {"form": form})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("home")
