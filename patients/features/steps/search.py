# -*- coding: utf-8 -*-
from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not

@given(u'que o Usuario se autentica')
def authentication(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8000/')
    
    username = context.driver.find_element_by_id('username')
    username.send_keys('larissa')
    password = context.driver.find_element_by_id('password')
    password.send_keys('1234')
    submit = context.driver.find_element_by_id('enter-button')
    submit.click()

@given(u'que o Usuario esta na tela de busca de pacientes')
def is_on_home_search(context):
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
    context.driver.close()

@when(u'o usuario digita o prontuario do Paciente')
def typing_pacient_report(context):
    pacient_name_input = context.driver.find_element_by_id('report')
    pacient_name_input.send_keys('808790')

@then(u'o sistema retorna os Pacientes com o prontuario digitado')
def return_pacient_report(context):
    pacient_report = context.driver.find_element_by_class_name('fi-male')
    pacient_report.text | should | equal_to('LEONARDO QXXXXXXXXXXXXILVA')
    pacient_report = context.driver.find_element_by_class_name('fi-clipboard-notes')
    pacient_report.text | should | equal_to('808790')
    context.driver.close()

@when(u'o usuario digita o nome da mae do Paciente')
def typing_patient_mothername(context):
    pacient_mothername = context.driver.find_element_by_id('mother_name')
    pacient_mothername.send_keys('Marfiza')

@then(u'o sistema retorna os Pacientes com o nome da mae digitado')
def return_patient_mothername(context):
    patients_name = context.driver.find_elements_by_class_name('fi-male')
    patients_mothername = context.driver.find_elements_by_class_name('fi-torso-female')

    patients_name[0].text | should | equal_to('ARIDEU CXXXXXXXXXXOPES')
    patients_mothername[0].text | should | equal_to('MARFIZA XXXXXXXXXXOPES')
    
    patients_name[2].text | should | equal_to('NILZA MXXXXXXXXXXXNTOS') 
    patients_mothername[1].text | should | equal_to('MARFIZA XXXXXXXAQUI')
      
    context.driver.close()

@when(u'o usuario digita a data de nascimento do Paciente')
def typing_birthday_only(context):
    assert False

@then(u'o sistema retorna os Pacientes com a data de nascimento digitada')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome e prontuario do Paciente')
def step_impl(context):
    assert False

@when(u'o usuario digita o nome, prontuario e nome da mae')
def typing_patient_name_report_mothername(context):
    name_input = context.driver.find_element_by_id('patient')
    report_input = context.driver.find_element_by_id('report')
    mothername_input = context.driver.find_element_by_id('mother_name')
    
    name_input.send_keys('Queilane')
    report_input.send_keys('417899')
    mothername_input.send_keys('Nao')

@then(u'o sistema retorna os Pacientes com o nome, prontuario e nome da mae digitado')
def return_name_report_mothername(context):
    patient_name = context.driver.find_element_by_class_name('fi-male')
    patient_report = context.driver.find_element_by_class_name('fi-clipboard-notes')
    patient_mothername = context.driver.find_element_by_class_name('fi-torso-female')

    patient_name.text | should | equal_to('QUEILANE BXXXISTA')
    patient_report.text | should | equal_to('417899')
    patient_mothername.text | should | equal_to('NAO XXXXXXMADO')

    context.driver.close()

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
#Implementando
@when(u'o usuario digita o nome da mae e data nascimento do Paciente')
def step_impl(context):
    context.driver.find_element_by_id("date").click()
    context.driver.find_element_by_xpath("//div[2]/div[3]/table/tbody/tr[3]/td[2]").click()
    context.driver.close()

@then(u'o sistema retorna os Pacientes com a nome da mae e data nascimento digitado')
def step_impl(context):
    assert False
