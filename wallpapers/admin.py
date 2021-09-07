from django.contrib import admin
from .models import City,Photo,Category,Tag

# Register your models here.

admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Tag)

