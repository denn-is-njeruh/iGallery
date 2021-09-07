from django.test import TestCase
from .models import Photo,City,Category


# Create your tests here.
class TestImageClass(TestCase):
  #Setup method
  def setUp(self):
    self.new_photo = Photo(photo_name = 'the_matrix', description ='the wallpaper is borrowed from the matrix movie', city='Chicago', category= 'movie', image='media/default.jpg')
    self.new_photo.save()

    self.new_city = City(name='Chicago')
    self.new_city.save()

    self.new_category = Category(category_name='movie')
    self.new_category.save()

  def tearDown(self):
    Photo.objects.all().delete()
    Category.objects.all().delete()
    City.objects.all().delete()

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

  def test_get_photos_by_id(self):
    # self.new_photo.save_photo()
    fetched_photo = Photo.get_photo_by_id(1)
    self.assertTrue(fetched_photo.id,1)

  def test_search_by_category(self):
    self.new_photo.save_photo()
    fetch_category = Category.objects.get(category_name='movie')
    self.assertTrue(fetch_category.category_name=='movie')

  def test_filter_by_location(self):
    self.new_photo.save_photo()
    fetched_location = City.objects.get(location_name='Washington DC')
    self.assertTrue(fetched_location.location_name=='Washington DC')

  def test_update_image(self):
    self.new_photo.save_photo()
    fetched = Photo.objects.get(photo_name = 'avengers')
    self.assertEqual(fetched.photo_name,'avengers')


class TestCityClass(TestCase):
  def setUp(self):
    self.new_city = City(name ='Hollywood')
    self.new_city.save()

  def test_save_city(self):
    self.new_city.save_city()
    cities = City.objects.all()
    self.assertTrue(len(cities)>0)

  def test_update_location(self):
    self.new_city.save_city()
    fetched = City.objects.get(name = 'Chicago')
    self.assertEqual(fetched.name,'Chicago')

class TestCategoryClass(TestCase):
  def setUp(self):
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