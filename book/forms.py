from django.forms import ModelForm

from .models import Book, Comment


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'body', 'author', 'publisher', 'price']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'recommend', 'star']

