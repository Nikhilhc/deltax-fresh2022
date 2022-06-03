from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from .views import ArtistView
from .views import SongsView

app_name = 'deltax_spotify'
urlpatterns = [
    path('artist/',ArtistView.as_view(),name='artist'),
    path('songs/',SongsView.as_view(),name='songs')
]
