# -*- coding: utf-8 -*-
from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not


@given(u'que o Usuario esta na tela de busca de pacientes')
def is_authenticated(context):
    context.driver = webdriver.Firefox()
    #Alterar porta do localhost
    context.driver.get('http://localhost:8000/consulta/')
    context.driver.title | should | equal_to('Home | Anato')

@given(u'aparece a tela de busca')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome do Paciente')
def typing_pacient_name(context):
    pacient_name_input = context.driver.find_element_by_id('patient')
    pacient_name_input.send_keys('Queilane')

@when(u'clica em buscar')
def click_search_button(context):
    search_button = context.driver.find_element_by_id('search-button')
    search_button.click()

@then(u'o sistema retorna os Pacientes com o nome digitado')
def return_pacient_name(context):
    pacient_name = context.driver.find_element_by_class_name('fi-male')
    pacient_name.text | should | equal_to('QUEILANE BXXXISTA')

@when(u'o usuario digita o prontuario do Paciente')
def typing_pacient_name(context):
    pacient_name_input = context.driver.find_element_by_id('report')
    pacient_name_input.send_keys('808790')

@then(u'o sistema retorna os Pacientes com o prontuario digitado')
def step_impl(context):
    pacient_report = context.driver.find_element_by_class_name('fi-male')
    pacient_report.text | should | equal_to('LEONARDO QXXXXXXXXXXXXILVA')
    pacient_report = context.driver.find_element_by_class_name('fi-clipboard-notes')
    pacient_report.text | should | equal_to('808790')


@when(u'o usuario digita o nome da mae do Paciente')
def typing_mothername_only(context):
    assert False

@then(u'o sistema retorna os Pacientes com o nome da mae digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita a data de nascimento do Paciente')
def typing_birthday_only(context):
    assert False

@then(u'o sistema retorna os Pacientes com a data de nascimento digitada')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome e prontuario do Paciente')
def step_impl(context):
    assert False

@then(u'o sistema retorna os Pacientes com a nome e prontuario digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome e nome da mae do Paciente')
def step_impl(context):
    assert False

@then(u'o sistema retorna os Pacientes com a nome e nome da mae digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome e data de nascimento do Paciente')
def step_impl(context):
    assert False

@then(u'o sistema retorna os Pacientes com a nome e data de nascimento digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita o prontuario e nome da mae do Paciente')
def step_impl(context):
    assert False

@then(u'o sistema retorna os Pacientes com a prontuario e nome da mae digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita o prontuario e data nascimento do Paciente')
def step_impl(context):
    assert False

@then(u'o sistema retorna os Pacientes com a prontuario e data nascimento digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome da mae e data nascimento do Paciente')
def step_impl(context):
    assert False

@then(u'o sistema retorna os Pacientes com a nome da mae e data nascimento digitado')
def step_impl(context):
    assert False
