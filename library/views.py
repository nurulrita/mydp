from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Genre
from .models import Page, Book
#from .forms import CategoryForm
#from .forms import PageForm
#from .forms import BookForm

def index(request):

    genre_list = Genre.objects.order_by('name')[:5]
    context_dict = {'genres': genre_list}

    return render(request, 'library/index.html', context_dict)

def genre(request, genre_name_slug):

    context_dict = {}

    try:
        genre = Genre.objects.get(slug=genre_name_slug)
        context_dict['genre_name'] = genre.name


        books = Book.objects.filter(genre=genre)


        context_dict['books'] = books
        context_dict['genre'] = genre
    
    except Genre.DoesNotExist:

        pass

    return render(request, 'library/genre.html', context_dict)


def book(request, genre_name_slug, book_slug):
    context_dict = {}
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
        book = Book.objects.get(genre=genre, slug=book_slug)
        context_dict['book_slug'] = book_slug
        context_dict['book'] = book
    except Book.DoesNotExist:
	    pass
    return render(request, 'library/book.html', context_dict)

