from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^login/', include('authentication.urls')),
    url(r'^examination/', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.home_search'),
    url(r'^home/$', 'authentication.views.home'),
    url(r'^resultados/$', 'core.views.search_results'),
    url(r'^paciente/(?P<records>\w*)$', 'core.views.patient_profile'),
)
