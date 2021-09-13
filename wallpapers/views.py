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


# def movie_wallpaper(request):
#   categories = Category.objects.all()
#   movie = Photo.objects.filter(category = categories)
#   return render(request, 'all-wallpapers/movie-wallpapers.html', {"movie": movie})


# def nature_wallpaper(request):
#   wallpapers = Photo.objects.order_by(category_name='nature')
#   return render(request, 'all-wallpapers/nature-wallpapers.html', {"wallpaper":wallpapers})


# def sport_wallpaper(request):
#   wallpaper = Photo.objects.filter()
#   return render(request, 'all-wallpapers/sport-wallpapers.html', {"wallpaper": wallpaper})


def search_results(request):
  if 'photo' in request.GET and request.GET["photo"]:
    search_term = request.GET.get("photo")
    searched_photo = Photo.search_by_category(search_term)
    message = f"{search_term}"
    return render(request, 'all_wallpapers/search.html',{"message":message, "photos":searched_photo})
  else:
    message = "The category you searched is not available"
  return render(request,'all_wallpapers/search.html',{"message":message})


def wallpaper(request,id):
  try:
    wallpaper = Photo.objects.filter(id = id)
  except Photo.DoesNotExist:
    raise Http404()
  return render(request,'photo_detail.html', {"wallpaper": wallpaper})

