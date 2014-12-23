# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from core.decorators import permission_required_with_403
from authentication.auth import authenticate_user_without_ldap, \
    SUCCESS, INACTIVE_USER, INVALID_LOGIN, LDAP_CONNECTION_ERROR
import json


def sign_in(request):
    if request.user.is_authenticated():
        return render_to_response(
            'home_search.html',
            context_instance=RequestContext(request)
        )

    if request.method == 'GET':
        return render_to_response(
            'sign_in.html',
            context_instance=RequestContext(request)
        )

    username = request.POST['username']
    password = request.POST['password']
    login_user = authenticate_user_without_ldap(request, username, password)
    warning_message = None

    if login_user == SUCCESS:
        return redirect('/')
    elif login_user == INACTIVE_USER:
        warning_message = "Solicitação realizada, aguarde confirmação."
    elif login_user == INVALID_LOGIN:
        warning_message = "Nome de usuário ou senha incorretos."
    elif login_user == LDAP_CONNECTION_ERROR:
        warning_message = "Ocorreu um erro na conexão. Tente novamente."

    return render_to_response(
        'sign_in.html',
        {'login_error': warning_message,
         'modal_error': True},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def log_out(request):
    logout(request)
    return redirect('/')


@permission_required_with_403('auth.change_user')
@login_required(login_url='/', redirect_field_name='')
def admin_painel(request):
    return render_to_response(
        'admin_painel.html',
        locals(),
        context_instance=RequestContext(request)
    )


@permission_required_with_403('auth.change_user')
@login_required(login_url='/', redirect_field_name='')
def update_user(request, id_user):
    user = User.objects.get(pk=id_user)

    if request.method == 'POST':
        user.is_active = str(user.id) in request.POST
        user.save()

    return render_to_response(
        'update_user.html',
        {'u': user},
        context_instance=RequestContext(request)
    )


def search_user(request, cpf):
    try:
        users = list(User.objects.filter(
            username__startswith=cpf).order_by('-date_joined'))
        status_code = 500
        serialize_users = serializers.serialize('json', users)
        json_data = json.loads(serialize_users)
        json_data = json.dumps({'users': json_data})
        response = HttpResponse(json_data, content_type='application/json')
    except:
        response = HttpResponse()

    return response
