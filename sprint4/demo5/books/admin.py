from django.contrib import admin
from .models import Book, BookMark

# Register your models here.
admin.site.register([Book, BookMark])
# admin.site.register(BookMark)
