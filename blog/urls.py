from django.urls import path
from .views import login_view, logout_view, home_view, register_view

urlpatterns = [
    path("", home_view, name='home'),
    path("login/", login_view, name='login'),
    path("sign-up/", register_view, name='sign-up'),
    path("logout/", logout_view, name='logout')
]
