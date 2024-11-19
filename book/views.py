from django.urls import reverse_lazy
from django.views import generic

from .models import Book
from .forms import BookForm


class BookListView(generic.ListView):
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all().order_by('-datetime_modified')


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'body', 'author', 'publisher', 'price', 'covers']
    template_name = 'book/book_create.html'
    context_object_name = 'form'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'body', 'author', 'price', 'covers']
    template_name = 'book/book_update.html'
    context_object_name = 'form'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'book/book_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book_list')
