from django.conf.urls import patterns, url
from .import views

urlpatterns = [
    url(r'^$', views.galery, name='galery'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	url(r'^photo/(?P<category_name_slug>[\w\-]+)/(?P<photo_slug>[\w\-]+)/$', views.photo, name='photo'),
]
