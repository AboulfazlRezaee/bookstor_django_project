from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Book
# Create your views here.


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    # paginate_by = 10
    context_object_name = 'books'
    # def book_detail(request, pk):
    #     book = get_object_or_404(Book, pk=pk)
    #     return render(request, 'books/book_detail.html', {'book': book})