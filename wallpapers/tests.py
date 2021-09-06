from django.test import TestCase
from .models import Image,Location,Category


# Create your tests here.
class TestImageClass(TestCase):
  #Setup method
  def setUp(self):
    self.new_image = Image(image_name = 'the_matrix', image_description ='the wallpaper is borrowed from the matrix movie', location='Hollywood', category= 'movie', image_path='media/gallery/the_matrix.jpg')

  def test_save_method(self):
    self.new_image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)

  def test_delete_method(self):
    self.new_image.save_image()
    filtered_object = Image.objects.filter(image_name='the_matrix')
    Image.delete_image(filtered_object)
    all_objects = Image.object.all()
    self.assertTrue(len(all_objects)==0)

  def tearDown(self):
    Image.objects.all().delete()
    Category.objects.all().delete()
    Location.objects.all().delete()

  def test_get_images_by_id(self):
    self.new_image.save_image()
    fetched_image = Image.get_image_by_id(1)
    self.assertEqual(fetched_image.id,1)

  def test_search_by_category(self):
    self.new_image.save_image()
    fetch_category = Category.objects.get(category_name='movie')
    self.assertTrue(fetch_category.category_name=='movie')

  def test_filter_by_location(self):
    self.new_image.save_image()
    fetched_location = Location.objects.get(location_name='Washington DC')
    self.assertTrue(fetched_location.location_name=='Washington DC')

  def test_update_image(self):
    self.new_image.save_image()
    fetched = Image.objects.get(image_name = 'avengers')
    self.assertEqual(fetched.image_name,'avengers')


class TestLocationClass(TestCase):
  def setUp(self):
    self.new_image = Image(image_name = 'the_matrix', image_description ='the wallpaper is borrowed from the matrix movie', location='Hollywood', category= 'movie', image_path='media/gallery/the_matrix.jpg')
    self.new_image.save()

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
  