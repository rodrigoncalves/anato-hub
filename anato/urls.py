# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^', include('authentication.urls')),
    url(r'^exame/', include('exam.urls')),
    url(r'^biopsia/', include('biopsy.urls')),
    url(r'^congelamento/', include('freezing.urls')),
    url(r'^citologia/', include('cytology.urls')),
    url(r'^necropsia/', include('necropsy.urls')),
    url(r'^imunohistoquimica/', include('immunohistochemical.urls')),

    url(r'^consulta/$', 'core.views.home_search'),
    url(r'^resultados/$', 'patients.views.search_results'),
    url(r'^paciente/(?P<patient_id>\w+)$', 'patients.views.patient_profile'),
)
