# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'freezing.views',
    url(r'^$', 'register_freezing'),
    url(r'^novo/$', 'new_freezing'),
)
