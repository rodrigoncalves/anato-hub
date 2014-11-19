# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anato.settings")

from behave import given, when, then
from selenium import webdriver
from should_dsl import should


@given(u'que o usuario acessa a url "{url}" e aparece a tela de login')
def accessing_the_system(context, url):
    context.driver = webdriver.Firefox()
    context.driver.get(url)
    context.driver.title | should | equal_to('Login | Anato HUB')


@when(u'o usuario digita seu nome: "{user}"')
def insert_username(context, user):
    username_input = context.driver.find_element_by_id('username')
    username_input.send_keys(user)


@when(u'digita a sua senha: "{password}"')
def insert_password(context, password):
    username_input = context.driver.find_element_by_id('password')
    username_input.send_keys(password)


@when(u'clica em Entrar')
def click_enter(context):
    context.driver.find_element_by_id('enter-button').click()


@then(u'autentica o usuario com sucesso')
def authenticate_user(context):
    page_loaded = context.driver.title
    page_loaded | should | equal_to('Home | Anato HUB')
    context.driver.close()


@then(u'o sistema retorna a mensagem de erro "{mensagem}"')
def returns_error_message(context, mensagem):
    text = context.driver.find_element_by_xpath(
        "//p[@id='error-message']/b").text
    text | should | equal_to(mensagem)


@then(u'o sistema nao permite que o botao entrar seja clicado')
def enter_button_deactivated(context):
    enter_button = context.driver.find_element_by_id('enter-button')
    disabled_attribute = enter_button.get_attribute('disabled')
    disabled_attribute | should | equal_to('true')
    context.driver.close()
