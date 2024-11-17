from django.shortcuts import render
from django.views import generic

from .models import Book
from .forms import BookForm


class BookListView(generic.ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'body', 'author', 'publisher', 'price']
    template_name = 'book/book_create.html'
    context_object_name = 'form'


    