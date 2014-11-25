# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'authentication.views',
    url(r'^$', 'sign_in'),
    url(r'^sair/$', 'log_out'),
    url(r'^autorizar/$', 'autorize_user'),
    url(r'^procurar/(?P<cpf>\d{1,11})$', 'search_user'),
)
