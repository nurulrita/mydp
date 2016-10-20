from django.shortcuts import render
from .models import Galery

def galery(request):
	galeries = Galery.objects.all()
	return render(request, 'galery/galery.html',
                 {'galeries': galeries})
