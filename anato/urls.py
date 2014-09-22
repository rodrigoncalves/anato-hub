from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^login/', include('authentication.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.home_search'),
)
