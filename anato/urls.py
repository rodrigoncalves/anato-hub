# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^login/', include('authentication.urls')),
    url(r'^exame/', include('exam.urls')),

    url(r'^$', 'authentication.views.sign_in'),
    url(r'^resultados/$', 'core.views.search_results'),
    url(r'^consulta/$', 'core.views.home_search'),
    url(r'^paciente/(?P<records>\w+)$', 'core.views.patient_profile'),
    url(r'^biopsia/$', 'biopsy.views.add_biopsy'),
    url(r'^biopsia/nova/$', 'biopsy.views.new_biopsy'),
    url(r'^necropsia/$', 'necropsy.views.add_necropsy'),
    url(r'^necropsia/nova/$', 'necropsy.views.new_necropsy'),
    url(r'^exame/novo/$', 'core.views.new_exam'),
)
