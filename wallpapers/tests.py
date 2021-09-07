from django.test import TestCase
from .models import Photo,Location,Category


# Create your tests here.
class TestImageClass(TestCase):
  #Setup method
  def setUp(self):
    self.new_photo = Photo(photo_name = 'the_matrix', description ='the wallpaper is borrowed from the matrix movie', location='Chicago', category= 'movie', image='media/default.jpg')

  def test_save_method(self):
    self.new_photo.save_photo()
    images = Photo.objects.all()
    self.assertTrue(len(images)>0)

  def test_delete_method(self):
    self.new_photo.save_photo()
    filtered_object = Photo.objects.filter(photo_name='the_matrix')
    Photo.delete_image(filtered_object)
    all_objects = Photo.object.all()
    self.assertTrue(len(all_objects)==0)

  def tearDown(self):
    Photo.objects.all().delete()
    Category.objects.all().delete()
    Location.objects.all().delete()

  def test_get_photos_by_id(self):
    self.new_photo.save_photo()
    fetched_photo = Photo.get_photo_by_id(1)
    self.assertEqual(fetched_photo.id,1)

  def test_search_by_category(self):
    self.new_photo.save_photo()
    fetch_category = Category.objects.get(category_name='movie')
    self.assertTrue(fetch_category.category_name=='movie')

  def test_filter_by_location(self):
    self.new_photo.save_photo()
    fetched_location = Location.objects.get(location_name='Washington DC')
    self.assertTrue(fetched_location.location_name=='Washington DC')

  def test_update_image(self):
    self.new_photo.save_photo()
    fetched = Photo.objects.get(photo_name = 'avengers')
    self.assertEqual(fetched.photo_name,'avengers')


class TestLocationClass(TestCase):
  def setUp(self):
    self.new_photo = Photo(photo_name = 'the_matrix', description ='the wallpaper is borrowed from the matrix movie', location='Hollywood', category= 'movie', image='media/default.jpg')
    self.new_photo.save()

    self.new_location = Location(location_name ='Hollywood')
    self.new_location.save()

  def test_save_location(self):
    self.new_location.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations)>0)

  def test_update_location(self):
    self.new_location.save_location()
    fetched = Location.objects.get(location_name = 'Chicago')
    self.assertEqual(fetched.location_name,'Chicago')

class TestCategoryClass(TestCase):
  
  def setUp(self):
    self.new_photo = Photo(photo_name = 'the_matrix', description ='the wallpaper is borrowed from the matrix movie', location='Chicago', category='movie', image='media/default.jpg')
    self.new_photo.save()

    self.new_category = Category(category_name='movie')
    self.new_category.save()

  def test_save_category(self):
    self.new_category.save_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories)>0)

  def test_update_category(self):
    self.new_category.save_category()
    fetched = Category.objects.get(category_name='sports')
    self.assertEqual(fetched.category_name,'sports')