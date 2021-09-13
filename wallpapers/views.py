from django.shortcuts import render,redirect
from django.http import Http404
from .models import Photo,Category

# Create your views here.
def all_wallpapers(request):
  category = request.GET.get('category')
  if category is None:
    wallpapers = Photo.objects.all()
  else:
    wallpapers = Photo.objects.filter(category__category_name = category)
  categories = Category.objects.all()
  return render(request, 'index.html', {"wallpapers": wallpapers,"categories": categories,})


def movie_wallpaper(request):
  movie_category = Category.objects.all()
  movie = Photo.objects.filter(movie_category)
  return render(request, 'all-wallpapers/movie-wallpapers.html', {"movie": movie})


# def nature_wallpaper(request):
#   wallpapers = Photo.objects.order_by(category_name='nature')
#   return render(request, 'all-wallpapers/nature-wallpapers.html', {"wallpaper":wallpapers})


# def sport_wallpaper(request):
#   wallpaper = Photo.objects.filter()
#   return render(request, 'all-wallpapers/sport-wallpapers.html', {"wallpaper": wallpaper})


def wallpaper(request,id):
  try:
    wallpaper = Photo.objects.filter(id = id)
  except Photo.DoesNotExist:
    raise Http404()
  return render(request,'photo_detail.html', {"wallpaper": wallpaper})

