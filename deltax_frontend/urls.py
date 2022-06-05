from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from .views import register_request,login_view,logout_view
from .views import Songs_page,artists_page,add_artist_ajax,add_song,get_artist_ajax,get_rating_ajax,put_rating_ajax
from django.conf.urls.static import static
from django.conf import settings

app_name = 'deltax_frontend'
urlpatterns = [
    path("register", register_request, name="register"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("", Songs_page, name="songs"),
    path("songs", Songs_page, name="songs"),
    path("artist", artists_page, name="artist"),
    path("add_artist", add_artist_ajax, name="add_artist"),
    path("add_song", add_song, name="add_song"),
    path("get_artist", get_artist_ajax, name="get_artist"),
    path("get_rating", get_rating_ajax, name="get_rating"),
    path("put_rating", put_rating_ajax, name="put_rating"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
