from django.contrib import admin
from .models import Educations, ReadingRoom, Reader, BookReader, Book

# Register your models here.

admin.site.register(Educations)
admin.site.register(ReadingRoom)
admin.site.register(Reader)
admin.site.register(BookReader)
admin.site.register(Book)