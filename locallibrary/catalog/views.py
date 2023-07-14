from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

# Create your views here.
def index(request):
    """View function for home page of site.""" 

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_of_genre = Genre.objects.all().count()

    books_with_2 = Book.objects.all().filter(title__contains='2').count()

    context= {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_of_genre': num_of_genre,
        'books_with_2': books_with_2
    }

    return render(request, 'index.html', context=context)

# def book_detail_view(request, primary_key):
#     try:
#         book = Book.objects.get(pk.primary_key)
#     except Book.DoesNotExist:
#         raise http404('Book does not exist')

#     return render(request, 'catalog/book_detail.html', context={'book': book})

from django.views import generic 

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    model = Author


