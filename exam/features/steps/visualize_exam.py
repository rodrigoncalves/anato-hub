# -*- coding: utf-8 -*-
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from should_dsl import should, should_not
from exam.models import Exam
from core.dynamic_import import import_class

@given(u'que o usuario acessa a url "{url}"')
def acessing_system(context, url):
    context.driver = webdriver.Firefox()
    context.driver.get(url)   

@given(u'efetua o login no sistema')
def system_login(context):
    username = context.driver.find_element_by_id('username')
    username.send_keys('admin')
    password = context.driver.find_element_by_id('password')
    password.send_keys('1234')
    submit = context.driver.find_element_by_id('enter-button')
    submit.click()

@given(u'realiza uma busca pelo nome do paciente "{patient_name}"')
def search_patient(context, patient_name):
    pacient_name_input = context.driver.find_element_by_id('patient')
    pacient_name_input.send_keys(patient_name)
    search_button = context.driver.find_element_by_id('search-button')
    search_button.click()

@given(u'clica em Ver Paciente')
def visualize_patient(context):
    context.driver.find_element_by_id('visualize_patient').click()

@when(u'o paciente nao possui exames')
def patient_whithout_exam(context):
    pass
    #url = context.driver.current_url
    #patient_id = url.split('/')[-1]
    #exams = Exam.objects.filter(patient=patient_id)
    #for exam in exams:
        #specif_exam = import_class(exam.exam_type)
        #specific_exam.objects.filter(exam_id = exam.id).delete()
    #exams.delete()

@then(u'o sistema exibe a mensagem "{message}"')
def system_return_message(context, message):
    system_message = context.driver.find_element_by_id('message')
    system_message.text | should | equal_to(message)