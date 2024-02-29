from django.urls import path, include

from . import views


app_name = "sitecharlie"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.i_login, name="login"),
    path("register/", views.register, name="register"),
]