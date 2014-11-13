# -*- coding: utf-8 -*-

from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not 
from core.tests.db_mock import DatabaseMock
from core.tests.utils import authentication

@given(u'que o Usuario esta autenticado')
def accessing_the_system(context):
    context.driver = webdriver.Firefox()
    authentication(context)

    mock=DatabaseMock()
    mock.create_patient()

@given(u'que o Usuario esta na tela de busca de pacientes')
def is_on_home_search(context):
    context.driver.get('http://localhost:8000/consulta/')
    context.driver.title | should | equal_to('Home | Anato')

@when(u'o usuario digita o nome do Paciente')
def typing_pacient_name(context):
    pacient_name_input = context.driver.find_element_by_id('patient')
    pacient_name_input.send_keys('Maria')

@when(u'clica em buscar')
def click_search_button(context):
    search_button = context.driver.find_element_by_id('search-button')
    search_button.click()

@then(u'o sistema retorna os Pacientes com o nome digitado')
def return_pacient_name(context):
    pacient_name = context.driver.find_element_by_class_name('fi-male')
    pacient_name.text | should | equal_to('MARIA GXXXXXXXXXXXILVA')
    context.driver.close()

#@given(u'aparece a tela de busca de paciente')
#def showing_registration_examination(context):
   # assert False
    #driver.find_element_by_id("patient").clear()
    #driver.find_element_by_id("patient").send_keys("maria")
    #driver.find_element_by_id("search-button").click()
    #context.driver.title | should | equal_to('Cadastro de Exame | Anato HUB')

@given(u'que o auxiliar acessa o sistema e esta autenticado')
def accessing_the_system(context):
    authentication(context)
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8000/novo/exame/')

@given(u'aparece a tela de cadastro de exame')
def showing_registration_examination(context):
    context.driver.title | should | equal_to('Cadastro de Exame | Anato HUB')


@when(u'o auxiliar digita todos os campos corretamente')
def insert_examination(context):
    driver.find_element_by_xpath("//div[@id='sizzle-1415806506192']/div/table/tbody/tr[3]/td[4]").click()
    driver.find_element_by_xpath("//div[@id='sizzle-1415806506192']/div/table/tbody/tr[3]/td[5]").click()
    driver.find_element_by_xpath("//div[@id='sizzle-1415806506192']/div/table/tbody/tr[3]/td[3]").click()
    driver.find_element_by_id("received_speciment").clear()
    driver.find_element_by_id("received_speciment").send_keys("material")
    driver.find_element_by_id("requesting_physician").clear()
    driver.find_element_by_id("requesting_physician").send_keys("fulano")
    driver.find_element_by_id("responsible_physician").clear()
    driver.find_element_by_id("responsible_physician").send_keys("ciclano")
    driver.find_element_by_xpath("//input[@value='Enviar']").click()
    

@when(u'clica em enviar')
def registration(context):
    context.driver.find_element_by_xpath("//input[@value='Enviar']").click()
    #driver.find_element_by_xpath("//input[@value='Enviar']").click()
    #examination = context.driver.find_element_by_name("Cadastrar")
    #actions = ActionChains(driver)
   # actions.click(examination)

@given(u'aparece a tela de cadastro de biopsia')
def showing_registration_examination(context):
    #context.driver.title | should | equal_to('Cadastro de Exame | Anato HUB')
    assert False

@when(u'o auxiliar digita todos os campos corretamente')
def insert_examination(context):
    assert False

@then(u'o sistema cadastra')
def registration_examitation(context):
    assert False

