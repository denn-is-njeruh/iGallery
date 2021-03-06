from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  url(r'^$', views.all_wallpapers, name='wallpapers'),
  url(r'^wallpaper/(?P<id>\d+)', views.wallpaper, name='wallpaper'),
  # url(r'^sports/'$, views.sport_wallpaper, name='sportWallpapers'),
  
  #url(r'^movie_wallpaper/', views.movie_wallpaper, name='movieWallpapers'),
  url(r'^search/', views.search_results, name='search_results')
  ]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 