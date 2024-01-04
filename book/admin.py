from django.contrib import admin
from .models import Book, BookIndex, Writer

# Register your models here.
admin.site.register(Book)
admin.site.register(BookIndex)
admin.site.register(Writer)
