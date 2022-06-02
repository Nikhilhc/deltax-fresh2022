from django.contrib import admin
from django.urls import path,include
from .views import Homepage

urlpatterns = [
    path('/home',Homepage,name='home')
]
