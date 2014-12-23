# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'authentication.views',
    url(r'^$', 'sign_in'),
    url(r'^painel/$', 'admin_painel'),
    url(r'^procurar/(?P<cpf>\w{1,11})$', 'search_user'),
    url(r'^sair/$', 'log_out'),
    url(r'^usuario/(?P<id_user>\w{1,11})$', 'update_user'),
)
