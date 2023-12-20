from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from .models import Book
# Create your views here.


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    def get_queryset(self):
        return Book.objects.filter(status=True)

# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'comments': book_comments})

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', ]

class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title','author','description', 'price', 'cover',]

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

