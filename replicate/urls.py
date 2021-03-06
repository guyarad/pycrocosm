# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from django.conf.urls import url

from . import views

app_name = 'replicate'
urlpatterns = [
	url(r'^(minute|hour|day)/$', views.catalog, name='catalog'),
	url(r'^(minute|hour|day)/([0-9]+)/$', views.catalog2, name='catalog2'),
	url(r'^(minute|hour|day)/([0-9]+)/([0-9]+)/$', views.catalog3, name='catalog3'),
	url(r'^(minute|hour|day)/([0-9]+)/([0-9]+)/([0-9]+).state.txt$', views.state, name='diffstate'),
	url(r'^(minute|hour|day)/([0-9]+)/([0-9]+)/([0-9]+).osc.gz$', views.diffgz, name='diffdatagz'),
	url(r'^(minute|hour|day)/([0-9]+)/([0-9]+)/([0-9]+).osc$', views.diff, name='diffdata'),
    url(r'^$', views.index, name='replicate'),
]
