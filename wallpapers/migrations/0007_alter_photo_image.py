# Generated by Django 3.2.7 on 2021-09-07 06:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallpapers', '0006_auto_20210907_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=cloudinary.models.CloudinaryField(default='/media/default.jpg', max_length=255, verbose_name='image'),
        ),
    ]
