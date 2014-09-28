from django.conf.urls import patterns, url


urlpatterns = patterns(
    'authentication.views',

    url(r'^entrar/$', 'sign_in'),
    url(r'^sair/$', 'log_out'),
)
