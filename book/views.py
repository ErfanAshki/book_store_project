from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, render

from .models import Book, Comment
from .forms import BookForm, CommentForm


class BookListView(generic.ListView):
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all().order_by('-datetime_modified')


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment_form = comment_form.save(commit=False)
            new_comment_form.book = book
            new_comment_form.user = request.user
            new_comment_form.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'book/book_detail.html',
                  {'book': book, 'comments': comments, 'comment_form': comment_form})


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'book/book_detail.html'
#     context_object_name = 'book'


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
