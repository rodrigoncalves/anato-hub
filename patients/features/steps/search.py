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
def search_screen(context):
    context.driver.get('http://localhost:8000/consulta/')
    context.driver.title | should | equal_to('Home | Anato')

@when(u'o usuario digita o nome do Paciente')
def patient_name(context):
    pacient_name_input = context.driver.find_element_by_id('patient')
    pacient_name_input.send_keys('MARIA EXXXXXXXXXXXXXXLEAL')

@when(u'clica em buscar')
def search_click(context):
    search_button = context.driver.find_element_by_id('search-button')
    search_button.click()

@then(u'o sistema retorna os Pacientes com o nome digitado')
def return_patient_name(context):
    pacient_name = context.driver.find_element_by_class_name('fi-male')
    pacient_name.text | should | equal_to('MARIA EXXXXXXXXXXXXXXLEAL')
    context.driver.close()

@when(u'o usuario digita o prontuario do Paciente')
def patient_report(context):
    pacient_name_input = context.driver.find_element_by_id('report')
    pacient_name_input.send_keys('5754106')

@then(u'o sistema retorna os Pacientes com o prontuario digitado')
def return_patient_report(context):
    pacient_report = context.driver.find_element_by_class_name('fi-male')
    pacient_report.text | should | equal_to('MARIA EXXXXXXXXXXXXXXLEAL')
    pacient_report = context.driver.find_element_by_class_name('fi-clipboard-notes')
    pacient_report.text | should | equal_to('5754106')
    context.driver.close()

@when(u'o usuario digita o nome da mae do Paciente')
def patient_mother_name(context):
    pacient_mothername = context.driver.find_element_by_id('mother_name')
    pacient_mothername.send_keys('MARILENE XXXXXXXXXXXOMES')

@then(u'o sistema retorna os Pacientes com o nome da mae digitado')
def return_mother_name(context):
    patients_name = context.driver.find_element_by_class_name('fi-male')
    patients_mothername = context.driver.find_element_by_class_name('fi-torso-female')

    patients_name.text | should | equal_to('MARIA EXXXXXXXXXXXXXXLEAL')
    patients_mothername.text | should | equal_to('MARILENE XXXXXXXXXXXOMES')
        
    context.driver.close()

@when(u'o usuario digita a data de nascimento do Paciente')
def patient_born_date(context):
    date_input = context.driver.find_element_by_id('date')
    date_input.send_keys('16/06/2005')

@then(u'o sistema retorna os Pacientes com a data de nascimento digitada')
def return_born_date(context):
    date = context.driver.find_element_by_xpath("//span[3]/i")
    date.text | should | start_with('16 de Junho de 2005')
    context.driver.close()

@then(u'o sistema retorna os Pacientes com a nome e prontuario digitado')
def return_name_report(context):
    return_patient_name(context)
    return_patient_report(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com a nome e nome da mae digitado')
def return_name_mother_name(context):
    return_patient_name(context)
    return_mother_name(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com a nome e data de nascimento digitado')
def return_name_born_date(context):
    return_patient_name(context)
    return_born_date(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com a prontuario e nome da mae digitado')
def return_report_mother_name(context):
    return_patient_report(context)
    return_mother_name(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com a prontuario e data nascimento digitado')
def return_report_born_date(context):
    return_patient_report(context)
    return_born_date(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com a nome da mae e data nascimento digitado')
def return_mother_name_born_date(context):
    return_mother_name(context)
    return_born_date(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com o nome, prontuario e nome da mae digitado')
def name_report_mother_name(context):
    return_patient_name(context)
    return_patient_report(context)
    return_mother_name(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com o nome, prontuario e data de nascimento digitado')
def return_name_report_born_date(context):
    return_patient_name(context)
    return_patient_report(context)
    return_born_date(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com o nome, nome da mãe e data de nascimento digitado')
def return_name_mother_name_born_date(context):
    return_patient_name(context)
    return_mother_name(context)
    return_born_date(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com o prontuario, nome da mae e data de nascimento digitado')
def return_report_mother_name_born_date(context):
    return_patient_report(context)
    return_mother_name(context)
    return_born_date(context)
    context.driver.close()

@then(u'o sistema retorna os Pacientes com o nome, prontuario, nome da mae e data de nascimento digitado')
def return_all_fields(context):

    return_patient_name(context)
    return_patient_report(context)
    return_mother_name(context)
    return_born_date(context)
    context.driver.close()

@when(u'o usuario nao digita nenhum dos campos')
def step_impl(context):
    pass

@then(u'o botao de busca deve estar desabilitado')
def step_impl(context):
    pass
