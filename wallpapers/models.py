from django.db import models
import datetime as dt
from django.utils import timezone

# Create your models here.
class Image(models.Model):
  image_name = models.CharField(max_length = 255)
  post_date = models.DateTimeField(auto_now_add=True)
  image_description = models.CharField(max_length=255)
  location = models.ForeignKey('Location', on_delete=models.CASCADE)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  image_view = models.ImageField(upload_to = 'images/', default=timezone.now)
  
  def __str__(self):
    return self.image_name


class Category(models.Model):
  category_name = models.CharField(max_length= 35)


class Location(models.Model):
  location_name = models.CharField(max_length= 50)


class Tag(models.Model):
  tag_name = models.CharField(max_length= 40)
