# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'exam.views',
    url(r'^novo/$', 'new_exam'),
    url(r'^registrar/$', 'register_exam'),
    url(r'^visualizar/(?P<exam_id>\d+)$', 'visualize_exam'),
)
