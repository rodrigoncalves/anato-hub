# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('authentication.views',
    url(r'^$', 'sign_in'),
    url(r'^sair/$', 'log_out'),
)
