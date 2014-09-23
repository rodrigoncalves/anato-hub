# -*- coding: utf-8 -*-
from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not


@given(u'que o Usuario esta autenticado')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8080/login/entrar/')
    assert False

@given(u'aparece a tela de busca')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome do Paciente')
def typing_patientname_only(context):
    patient_name_input = context.driver.find_element_by_id('patient_name')
    patient_name_input.send_keys('jose eduardo barboza')

@when(u'clica em buscar')
def step_impl(context):
    assert False

@then(u'o sistema retorna os Pacientes com o nome digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita o prontuario do Paciente')
def typing_patientreport_only(context):
    patient_report_input = context.driver.find_element_by_id('patient_report')
    patient_report_input.send_keys('123456')

@then(u'o sistema retorna os Pacientes com o prontuario digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome da mae do Paciente')
def typing_mothername_only(context):
    mother_name_input = context.driver.find_element_by_id('mother_name')
    mother_name_input.send_keys('paola coelho')

@then(u'o sistema retorna os Pacientes com o nome da mae digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita a data de nascimento do Paciente')
def typing_birthday_only(context):
    birthday_input = context.driver.find_element_by_id('birthday')
    birthday_input.send_keys('28/04/1990')

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
