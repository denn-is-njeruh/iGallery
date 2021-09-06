from django.contrib import admin
from .models import Image,Category,Location,Tag

# Register your models here.

admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Tag)

