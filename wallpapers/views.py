from django.shortcuts import render,redirect
from django.http import Http404

# Create your views here.
def welcome(request):
  return render(request, 'welcome.html')

def movie_wallpaper(request):
  return render(request, 'all-wallpapers/movie-wallpapers.html')


def nature_wallpaper(request):
  return render(request, 'all-wallpapers/nature-wallpapers.html')


def sport_wallpaper(request):
  return render(request, 'all-wallpapers/sport-wallpapers.html')
