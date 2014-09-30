from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^login/', include('authentication.urls')),
    url(r'^examination/', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'authentication.views.sign_in'),
    url(r'^resultados/$', 'core.views.search_results'),
    url(r'^consulta/$', 'core.views.home_search'),
    url(r'^paciente/(?P<records>\w*)$', 'core.views.patient_profile'),
    url(r'^nova/biopsia/$', 'core.views.new_biopsy'),
)
