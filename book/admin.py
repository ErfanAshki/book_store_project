from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publisher', 'price', 'datetime_created']
    ordering = ['id']


admin.site.register(Book, BookAdmin)
