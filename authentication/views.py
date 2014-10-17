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
    error_message = None
    print login_user
    if login_user == SUCCESS:
        return redirect('/')
    elif login_user == INACTIVE_USER:
        error_message = "Solicitação realizada, aguarde confirmação."
    elif login_user == INVALID_LOGIN:
        error_message = "Usuário ou senha estão inválidos."
    elif login_user == LDAP_CONNECTION_ERROR:
        error_message = "Um erro ocorreu com a conexão. Tente novamente."

    return render_to_response('sign_in.html',
        {'login_error': error_message, 'modal_error': True},
        context_instance=RequestContext(request)
    )

@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def home(request):
    return render_to_response('home.html')
