from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from .views import register_request,login_view,logout_view
from .views import homepage

app_name = 'deltax_frontend'
urlpatterns = [
    path("register", register_request, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("home", homepage, name="home")
]
