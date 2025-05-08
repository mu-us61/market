from django.urls import path
from .views import MyLoginView, MyRegisterView, MyLogoutView

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("register/", MyRegisterView.as_view(), name="register"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
]
