# -*- coding: utf-8 -*-
from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not


@given(u'que o usuario acessa o sistema')
def accessing_the_system(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://192.168.0.9:8000/login/entrar/')


@given(u'aparece a tela de login')
def showing_login(context):
    context.driver.title | should | equal_to('Login | Anato HUB')


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
    username_input = context.driver.find_element_by_id('username')
    username_input.send_keys('teste')


@when(u'o usuario digita somente seu nome')
def typing_username_only(context):
    username_input = context.driver.find_element_by_id('username')
    username_input.send_keys('teste')


@then(u'o sistema nao permite que o botao entrar seja clicado')
def enter_button_deactivated(context):
    enter_button = context.driver.find_element_by_id('enter-button')
    disabled_attribute = enter_button.get_attribute('disabled')
    disabled_attribute | should | equal_to('true')
    context.driver.close()
