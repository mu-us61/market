from django.shortcuts import render, redirect
from django.contrib import messages  # TODO gercekten burasimi yeri kontrol et
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout
from django.views.generic import CreateView

# from django.contrib.auth.forms import UserCreationForm
from .forms import MyUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
# User = get_user_model()


class MyRegisterView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "app_users/register.html"
    # template_name = "base.html"


class MyLoginView(LoginView):
    redirect_authenticated_user = True  # auto redirect logged-in users
    # success_url = reverse_lazy("home")  # optional: force redirect URL
    template_name = "app_users/login.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'My Awesome Login Page'
    #     return context


class MyLogoutView(LogoutView):
    pass
    # template_name = "registration/logged_out.html"
