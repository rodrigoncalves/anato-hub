# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^login/', include('authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'authentication.views.sign_in'),
    url(r'^resultados/$', 'core.views.search_results'),
    url(r'^consulta/$', 'core.views.home_search'),
    url(r'^paciente/(?P<records>\w+)$', 'core.views.patient_profile'),
    url(r'^biopsia/nova$', 'core.views.new_biopsy'),
    url(r'^necropsia/nova$', 'core.views.new_necropsy'),
    url(r'^biopsia/nova/salvar/$', 'biopsy.views.add_biopsy'),
    url(r'^necropsia/nova/salvar/$', 'necropsy.views.add_necropsy'),
    url(r'^novo/exame/$', 'core.views.new_exam'),

)
