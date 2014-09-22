# -*- coding: utf-8 -*-
from behave import given, when, then
# from selenium import webdriver
# from should_dsl import should, should_not


@given(u'que o usuario acessa o sistema')
def accessing_the_system(context):
    assert False


@given(u'aparece a tela de login')
def showing_login(context):
    assert False


@when(u'o usuario digita seu nome')
def insert_username(context):
    assert False


@when(u'digita a sua senha')
def insert_password(context):
    assert False


@then(u'autentica o usuario com sucesso')
def authenticate_user(context):
    assert False


@then(u'o sistema nao consegue autenticar o usuario no LDAP')
def authenticate_user_fail(context):
    assert False


@then(u'retorna uma mensagem "{mensagem}"')
def returns_message(context, mensagem):
    assert False


@when(u'o usuario digita somente sua senha')
def typing_password_only(context):
    assert False


@when(u'o usuario digita somente seu nome')
def typing_username_only(context):
    assert False


@then(u'o sistema nao permite que o botao entrar seja clicado')
def enter_button_deactivated(context):
    assert False
