# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from authentication.auth import authenticate_user, SUCCESS, INACTIVE_USER, \
    INVALID_LOGIN, LDAP_CONNECTION_ERROR

def sign_in(request):
    if request.user.is_authenticated():
        return render_to_response('home_search.html',
            context_instance=RequestContext(request)
        )

    if request.method == 'GET':
        return render_to_response('sign_in.html',
            context_instance=RequestContext(request)
        )

    username = request.POST.get('username')
    password = request.POST.get('password')
    login_user = authenticate_user(request=request, username=username, password=password)
    warning_message = None

    if login_user == SUCCESS:
        return redirect('/')
    elif login_user == INACTIVE_USER:
        warning_message = "Solicitação realizada, aguarde confirmação."
    elif login_user == INVALID_LOGIN:
        warning_message = "Nome de usuário ou senha incorretos."
    elif login_user == LDAP_CONNECTION_ERROR:
        warning_message = "Ocorreu um erro na conexão. Tente novamente."

    return render_to_response('sign_in.html',
        {'login_error': warning_message, 'modal_error': True},
        context_instance=RequestContext(request)
    )

@login_required(login_url='/')
def log_out(request):
    logout(request)
    return redirect('/')
