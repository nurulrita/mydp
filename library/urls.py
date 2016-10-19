from django.conf.urls import patterns, url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^genre/(?P<genre_name_slug>[\w\-]+)/$', views.genre, name='genre'),
	url(r'^book/(?P<genre_name_slug>[\w\-]+)/(?P<book_slug>[\w\-]+)/$', views.book, name='book'),
]
