from django.contrib import admin
from .models import Photo,Category,Location,Tag

# Register your models here.

admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Tag)

