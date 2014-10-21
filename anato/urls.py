# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^exame/', include('exam.urls')),

    url(r'^$', 'authentication.views.sign_in'),
    url(r'^sair/$', 'authentication.views.log_out'),
    url(r'^resultados/$', 'patients.views.search_results'),
    url(r'^consulta/$', 'patients.views.home_search'),
    url(r'^paciente/(?P<records>\w+)$', 'core.views.patient_profile'),
    url(r'^exame/novo/$', 'exam.views.new_exam'),
    url(r'^biopsia/$', 'biopsy.views.add_biopsy'),
    url(r'^biopsia/nova/$', 'biopsy.views.new_biopsy'),
    url(r'^citologia/nova/$', 'cytology.views.new_cytology'),
    url(r'^necropsia/$', 'necropsy.views.add_necropsy'),
    url(r'^necropsia/nova/$', 'necropsy.views.new_necropsy'),
    url(r'^imunohistoquimica/$', 'immunohistochemical.views.add_immunohistochemical'),
    url(r'^imunohistoquimica/nova/$', 'immunohistochemical.views.new_immunohistochemical'),
)
