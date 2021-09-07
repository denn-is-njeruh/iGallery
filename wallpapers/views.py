from django.shortcuts import render,redirect
from django.http import Http404
from .models import Photo,Location,Category

# Create your views here.
def all_wallpaper(request):
  wallpaper = Photo.objects.all()
  category = Category.objects.all()
  return render(request, 'all-wallpapers/wallpaper.html', {"wallpaper": wallpaper,"category":category})


def movie_wallpaper(request):
  wallpaper = Photo.objects.get(pk=1)
  return render(request, 'all-wallpapers/movie-wallpapers.html', {"wallpaper": wallpaper})


def nature_wallpaper(request):
  return render(request, 'all-wallpapers/nature-wallpapers.html')


def sport_wallpaper(request):
  return render(request, 'all-wallpapers/sport-wallpapers.html')

# def image(request,image_id):
#   try:
#     image = Image.objects.get(id=image_id)
#   except Image.DoesNotExist:
#     raise Http404()
#   return render(request,'all-wallpapers/wallpaper.html', {"image":image,})

