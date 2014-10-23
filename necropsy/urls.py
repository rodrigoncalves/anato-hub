# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'necropsy.views',
    url(r'^$', 'add_necropsy'),
    url(r'^nova/$', 'new_necropsy'),
)
