# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('cytology.views',
    url(r'^$', 'add_cytology'),
    url(r'^nova/$', 'new_cytology'),
)
