# -*- coding: utf-8 -*-

from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not


@given(u'que o auxiliar acessa o sistema e esta autenticado')
def accessing_the_system(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8000/novo/exame/')


@given(u'aparece a tela de cadastro de exame')
def showing_registration_examination(context):
    context.driver.title | should | equal_to('Cadastro de Exame | Anato HUB')


@when(u'o auxiliar digita todos os campos corretamente')
def insert_examination(context):
    assert False


@when(u'clica em cadastrar')
def registration(context):
    examination = context.driver.find_element_by_name("Cadastrar")
    actions = ActionChains(driver)
    actions.click(examination)


@then(u'o sistema cadastra o exame')
def registration_examitation(context):
    assert False


@then(u'retorna uma mensagem "{mensagem}"')
def returns_message(context, mensagem):
    assert False


@when(u'o auxiliar digita somente alguns campos obrigatorios')
def insert_examination(context):
    assert False


@then(u'o sistema nao cadastra o exame')
def registration_examitation_fail(context):
    assert False


@when(u'o auxiliar digita algum campo incorretamente')
def insert_examination(context):
    assert False
