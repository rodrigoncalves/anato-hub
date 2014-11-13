# -*- coding: utf-8 -*-
from behave import given, when, then
from selenium import webdriver
from should_dsl import should


@given(u'que o usuário abre o navegador')
def open_browser(context):
    context.driver = webdriver.Firefox()


@when(u'acessa a url "{url}"')
def access_localhost(context, url):
    context.driver.get(url)


@then(u'o sistema exibe a pagina de login')
def open_login_page(context):
    context.driver.title | should | equal_to('Login | Anato HUB')
    context.driver.close()
