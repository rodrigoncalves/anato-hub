# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'biopsy.views',
    url(r'^$', 'register_biopsy'),
    url(r'^nova/$', 'new_biopsy'),
)
