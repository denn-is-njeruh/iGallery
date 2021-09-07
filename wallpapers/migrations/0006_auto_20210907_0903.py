# Generated by Django 3.2.7 on 2021-09-07 06:03

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallpapers', '0005_alter_image_image_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_name', models.CharField(max_length=255)),
                ('description', models.CharField(default=django.utils.timezone.now, max_length=255)),
                ('image', cloudinary.models.CloudinaryField(default='/media/default.jpg', max_length=255, verbose_name='images')),
                ('category', models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='wallpapers.category')),
                ('location', models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='wallpapers.location')),
            ],
            options={
                'ordering': ['photo_name'],
            },
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]