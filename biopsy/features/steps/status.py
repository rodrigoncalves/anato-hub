# -*- coding: utf-8 -*-

from behave import given, when, then
from selenium import webdriver
from should_dsl import should, should_not 
from core.tests.db_mock import DatabaseMock
from core.tests.utils import authentication

@given(u'que o auxiliar acessa o sistema e esta autenticado')
def accessing_the_system(context):
    context.driver = webdriver.Firefox()
    authentication(context)

    mock=DatabaseMock()
    mock.create_patient()

@given(u'aparece a tela de busca de paciente')
def showing_registration_examination(context):
    driver.find_element_by_id("patient").clear()
    driver.find_element_by_id("patient").send_keys("maria")
    driver.find_element_by_id("search-button").click()
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
    

@when(u'clica em cadastrar')
def registration(context):
    driver.find_element_by_xpath("//input[@value='Enviar']").click()
    #examination = context.driver.find_element_by_name("Cadastrar")
    #actions = ActionChains(driver)
   # actions.click(examination)


@then(u'o sistema cadastra a biopsia')
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
