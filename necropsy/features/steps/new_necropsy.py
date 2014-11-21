# -*- coding: utf-8 -*-

from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not
from core.tests.utils import authentication


@given(u'que o usuario entra no sistema')
def user_enter(context):
    authentication(context)


@given(u'realiza uma busca de paciente')
def patient_search(context):
    context.driver.title | should | equal_to("Home | Anato")
    patient = context.driver.find_element_by_id('patient')
    patient.send_keys("Maria")
    search = context.driver.find_element_by_id('search-button')
    search.click()

@given(u'escolhe o paciente')
def select_patient(context):
    search = context.driver.find_element_by_css_selector('button.postfix')
    search.click()


@given(u'cadastra um exame do tipo Necropsia')
def register_exam(context):
    context.driver.find_element_by_id('speciment_collection_date').click()
    context.driver.find_element_by_xpath("//div[9]/div/table/tbody/tr[4]/td[5]").click()
    context.driver.find_element_by_id('request_date').click()
    context.driver.find_element_by_xpath("//div[10]/div/table/tbody/tr[4]/td[5]").click()
    context.driver.find_element_by_id('receipt_date').click()
    context.driver.find_element_by_xpath("//div[11]/div/table/tbody/tr[4]/td[5]").click()
    context.driver.find_element_by_id('received_speciment').send_keys('materia1')
    context.driver.find_element_by_id('requesting_physician').send_keys('medico1')
    context.driver.find_element_by_id('responsible_physician').send_keys('medico2')
    context.driver.find_element_by_xpath("//select[@id='exam_type']/option[text()='Necrópsia']").click()
     
    context.driver.find_element_by_id('send-button').click()
    
    

@when(u'aparece a tela de cadastro de necropsia')
def register_biopsy_screen(context):
    assert False
    

@then(u'o sistema cadastra a necropsia')
def register_biopsy(context):
    context.driver.find_element_by_id('send-biopsy').click()
