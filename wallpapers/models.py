from django.db import models
from django.utils import timezone

# Create your models here.
class Image(models.Model):
  image_name = models.CharField(max_length = 255)
  post_date = models.DateTimeField(auto_now_add=True)
  image_description = models.CharField(max_length=255, default=timezone.now)
  location = models.ForeignKey('Location', on_delete=models.CASCADE, default=timezone.now)
  category = models.ForeignKey('Category', on_delete=models.CASCADE, default=timezone.now)
  image_view = models.ImageField(upload_to = 'images/', default=timezone.now)
  
  def __str__(self):
    return self.image_name
  
  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  @classmethod
  def search_by_category(cls,search_term):
    image = cls.objects.filter(category__icontains=search_term)
    return image

  @classmethod
  def get_image_by_id(cls,incoming_id):
    image_result = cls.objects.get(id=incoming_id)
    return image_result

  @classmethod
  def update_image(cls,current_value,new_value):
    fetched_object = Image.objects.filter(image_name = current_value).update(image_name = new_value)
    return fetched_object

  @classmethod
  def filter_by_location(cls,location):
    filtered_result = cls.objects.filter(image_location__location_name__icontains = location)
    return filtered_result


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


class Location(models.Model):
  location_name = models.CharField(max_length= 50)

  def __str__(self):
    return self.location_name

  def save_location(self):
    self.save()

  @classmethod
  def update_location(cls,current_value,new_value):
      fetched_location = Location.objects.filter(location_name = current_value).update(location_name = new_value)
      return fetched_location


class Tag(models.Model):
  tag_name = models.CharField(max_length= 40)

  def __str__(self):
    return self.tag_name