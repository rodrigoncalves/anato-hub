# -*- coding: utf-8 -*-
from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not


@given(u'que o Usuario esta autenticado')
def step_impl(context):
    assert False

@given(u'aparece a tela de busca')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome do Paciente')
def typing_patientname_only(context):
    assert False

@when(u'clica em buscar')
def step_impl(context):
    assert False

@then(u'o sistema retorna os Pacientes com o nome digitado')
def step_impl(context):
    assert False

@when(u'o usuario digita o prontuario do Paciente')
def typing_patientreport_only(context):
    assert False

@then(u'o sistema retorna os Pacientes com o prontuario digitado')
def step_impl(context):
    assert False

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
