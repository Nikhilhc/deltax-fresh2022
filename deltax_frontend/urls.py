from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from .views import register_request,login_view,logout_view
from .views import Songs_page,artists_page,add_artist_ajax,add_song,get_artist_ajax
from django.conf.urls.static import static
from django.conf import settings

app_name = 'deltax_frontend'
urlpatterns = [
    path("register", register_request, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("songs", Songs_page, name="songs"),
    path("artist", artists_page, name="artist"),
    path("add_artist", add_artist_ajax, name="add_artist"),
    path("add_song", add_song, name="add_song"),
    path("get_artist", get_artist_ajax, name="get_artist"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
