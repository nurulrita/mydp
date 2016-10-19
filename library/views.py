from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Category
from .models import Page, Book
#from .forms import CategoryForm
#from .forms import PageForm
#from .forms import BookForm

def index(request):

    category_list = Category.objects.order_by('name')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'library/index.html', context_dict)

def category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name


        books = Book.objects.filter(category=category)


        context_dict['books'] = books
        context_dict['category'] = category
    
    except Category.DoesNotExist:

        pass

    return render(request, 'library/category.html', context_dict)


def book(request, category_name_slug, book_title):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        book = Book.objects.get(category=category, slug=book_title)
        context_dict['book_title'] = book_title
        context_dict['book'] = book
    except Book.DoesNotExist:
	    pass
    return render(request, 'library/book.html', context_dict)

