from django.contrib import admin

from .models import Book, Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publisher', 'price', 'datetime_created']
    ordering = ['id']


admin.site.register(Book, BookAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'text', 'star', 'recommend', 'is_active', 'datetime_created']
    ordering = ['-datetime_created']


admin.site.register(Comment, CommentAdmin)

