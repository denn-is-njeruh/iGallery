# Generated by Django 3.2.7 on 2021-09-07 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallpapers', '0009_alter_photo_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallpapers.category'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallpapers.city'),
        ),
    ]
