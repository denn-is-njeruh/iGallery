from django.test import TestCase
from .models import Image,Location,Category


# Create your tests here.
class TestImageClass(TestCase):
  #Setup method
  def setUp(self):
    self.new_image = Image(image_name = 'the_matrix', image_description ='the wallpaper is borrowed from the matrix movie', location='Hollywood', category= 'movie', image_path='media/gallery/the_matrix.jpg')

  def test_save_method(self):
    self.image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)

  def tearDown(self):
    Image.objects.all().delete()
    Category.objects.all().delete()
    Location.objects.all().delete()

  def test_get_images_by_id(self):
    images_id = Image.get_image_by_id()
    self.assertTrue(len(images_id)==0)