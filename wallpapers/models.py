from django.db import models
import datetime as dt
from django.utils import timezone

# Create your models here.
class Image(models.Model):
  image_name = models.CharField(max_length = 255)
  post_date = models.DateTimeField(auto_now_add=True)
  image_view = models.ImageField(upload_to = 'images/', default=timezone.now)
  
  def __str__(self):
    return self.image_name