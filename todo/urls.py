from django.conf.urls import patterns, url
from .views import (
	activity_list,
	del_activity,
	)


urlpatterns =[
    url(r'^$', activity_list, name='activity_list'),
    url(r'^todo/(?P<pk>[0-9]+)/delete/$', del_activity, name='del_activity'),
]
