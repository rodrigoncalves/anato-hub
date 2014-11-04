# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'immunohistochemical.views',
    url(r'^$', 'add_immunohistochemical'),
    url(r'^nova/$', 'new_immunohistochemical'),
)
