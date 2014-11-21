# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^', include('authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^autopsia/$', 'necropsy.views.register_necropsy'),
    url(r'^biopsia/$', 'biopsy.views.register_biopsy'),
    url(r'^citologia/$', 'cytology.views.register_cytology'),
    url(r'^congelamento/$', 'freezing.views.register_freezing'),
    url(r'^consulta/$', 'core.views.home_search'),
    url(r'^exame/', include('exam.urls')),
    url(r'^imunohistoquimica/$', 'immunohistochemical.views.register_immunohistochemical'),
    url(r'^paciente/(?P<patient_id>\w+)$', 'patients.views.patient_profile'),
    url(r'^resultados/$', 'patients.views.search_results'),
)
