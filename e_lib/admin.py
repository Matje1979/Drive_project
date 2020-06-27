from django.contrib import admin
from .models import Book, Folder, UpdateLinks
# Register your models here.

admin.site.register(Book)
admin.site.register(Folder)
admin.site.register(UpdateLinks)

