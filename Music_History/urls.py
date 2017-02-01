"""Music_History URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.conf.urls import url, include
from music_history_api import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin

router = DefaultRouter()
router.register(r'songs', views.SongViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'genres', views.GenreViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

]
