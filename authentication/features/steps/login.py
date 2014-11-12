# -*- coding: utf-8 -*-

from behave import given, when, then
from selenium import webdriver
from should_dsl import should


@given(u'que o usuario acessa o sistema')
def accessing_the_system(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8000/')


@given(u'aparece a tela de login')
def showing_login(context):
    context.driver.title | should | equal_to('Login | Anato HUB')


@when(u'o usuario digita seu nome')
def insert_username(context):
    username_input = context.driver.find_element_by_id('username')
    username_input.send_keys('test_user')


@when(u'digita a sua senha')
def insert_password(context):
    username_input = context.driver.find_element_by_id('password')
    username_input.send_keys('123456')


@then(u'autentica o usuario com sucesso')
def authenticate_user(context):
    assert False


@then(u'o sistema nao consegue autenticar o usuario no LDAP')
def authenticate_user_fail(context):
    assert False


@then(u'retorna uma mensagem "{mensagem}"')
def returns_message(context, mensagem):
    assert False


@then(u'o sistema nao consegue conectar no LDAP')
def cant_connect_ldap(context):
    assert False


@then(u'retorna a mensagem de erro "{mensagem}"')
def returns_error_message(context, mensagem):
    assert False


@then(u'o sistema nao permite que o botao entrar seja clicado')
def enter_button_deactivated(context):
    enter_button = context.driver.find_element_by_id('enter-button')
    disabled_attribute = enter_button.get_attribute('disabled')
    disabled_attribute | should | equal_to('true')
    context.driver.close()
