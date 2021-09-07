from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField
from cloudinary.models import CloudinaryField

# Create your models here.
class Photo(models.Model):
  photo_name = models.CharField(max_length = 255)
  description = models.TextField(default=1)
  image = CloudinaryField('image', default='/media/default.jpg')
  category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
  city = models.ForeignKey('City', on_delete=models.CASCADE,default=1)
  
  def __str__(self):
    return self.photo_name
  
  def save_photo(self):
    self.save()

  def delete_photo(self):
    self.delete()

  @classmethod
  def search_by_category(cls,search_term):
    photo = cls.objects.filter(category__icontains=search_term)
    return photo

  @classmethod
  def get_photo_by_id(cls,photo_id):
    photo_result = cls.objects.filter(id=photo_id)
    return photo_result

  @classmethod
  def update_image(cls,current_value,new_value):
    fetched_object = Photo.objects.filter(photo_name = current_value).update(photo_name = new_value)
    return fetched_object

  @classmethod
  def filter_by_location(cls,location):
    filtered_result = cls.objects.filter(photo_location__location_name__icontains = location)
    return filtered_result

  class Meta:
    ordering = ['photo_name']


class Category(models.Model):
  category_name = models.CharField(max_length= 35)

  def __str__(self):
    return self.category_name

  def save_category(self):
    self.save()

  @classmethod
  def update_category(cls,current_value,new_value):
    fetched_category = Category.objects.filter(category_name = current_value).update(category_name = new_value)
    return fetched_category


class City(models.Model):
  name = models.CharField(max_length=50)


  def __str__(self):
    return self.name

  def save_city(self):
    self.save()

  @classmethod
  def update_city(cls,current_value,new_value):
      fetched_city = City.objects.filter(name = current_value).update(name = new_value)
      return fetched_city


class Tag(models.Model):
  tag_name = models.CharField(max_length= 40)

  def __str__(self):
    return self.tag_name