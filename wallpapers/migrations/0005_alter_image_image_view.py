# Generated by Django 3.2.7 on 2021-09-06 19:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallpapers', '0004_alter_image_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_view',
            field=cloudinary.models.CloudinaryField(default='/media/default.jpg', max_length=255, verbose_name='images'),
        ),
    ]