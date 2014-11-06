# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'exam.views',
    url(r'^(?P<exam_id>\d+)$', 'visualize_exam'),
    url(r'^novo/$', 'new_exam'),
    url(r'^registrar/$', 'register_exam'),
    url(r'^atualizar/(?P<exam_id>\d+)$', 'update_exam'),
    url(r'^atualizar/exame-especifico/(?P<exam_id>\d+)$', 'update_specific_exam'),
    url(r'^registrar_atualizacao/$', 'register_update_exam'),
)
