from django.conf.urls import patterns, url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	url(r'^book/(?P<category_name_slug>[\w\-]+)/(?P<book_title>[\w\-]+)/$', views.book, name='book'),
]
