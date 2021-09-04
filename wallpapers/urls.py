from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  url(r'^$',views.welcome, name='welcome'),
  url(r'^movies/', views.movie_wallpaper, name='movieWallpapers'),
  url(r'^sports/', views.sport_wallpaper, name='sportWallpapers'),
  url(r'^nature/', views.nature_wallpaper, name='natureWallpapers')
  ]