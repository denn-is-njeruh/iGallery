from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  url(r'^$', views.all_wallpapers, name='wallpapers'),
  # url(r'^sports/', views.sport_wallpaper, name='sportWallpapers'),
  url(r'^photo/<int:pk>', views.wallpaper, name='photos'),
  url(r'^movie_wallpaper', views.movie_wallpaper, name='movieWallpapers'),
  ]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 