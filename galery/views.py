from django.shortcuts import render
from .models import Galery
from .models import Category

def galery(request):
	galeries = Galery.objects.all()
	return render(request, 'galery/galery.html',
                 {'galeries': galeries})

def category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name


        galeries = Galery.objects.filter(category=category)


        context_dict['galeries'] = galeries
        context_dict['category'] = category
    
    except Galery.DoesNotExist:

        pass

    return render(request, 'galery/category.html', context_dict)
    
def photo(request, category_name_slug, photo_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        photo = Galery.objects.get(category=category, slug=photo_slug)
        context_dict['photo_slug'] = photo_slug
        context_dict['photo'] = photo
    except Galery.DoesNotExist:
	    pass
    return render(request, 'galery/photo.html', context_dict)
    
    
