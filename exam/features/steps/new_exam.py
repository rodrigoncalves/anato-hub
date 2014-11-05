# -*- coding: utf-8 -*-

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from should_dsl import should, should_not

def authentication(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8000/')

    username = context.driver.find_element_by_id('username')
    username.send_keys('ana')
    password = context.driver.find_element_by_id('password')
    password.send_keys('root')
    submit = context.driver.find_element_by_id('enter-button')
    submit.click()

@given(u'que o auxiliar acessa o sistema e esta autenticado')
def accessing_the_system(context):
    authentication(context)
    context.driver = webdriver.Firefox()
    context.driver.get('http://127.0.0.1:8000/exame/novo/')


@given(u'aparece a tela de cadastro de exame')
def showing_registration_examination(context):
    context.driver.title | should | equal_to('Cadastro de Exame | Anato HUB')


@when(u'o auxiliar digita todos os campos corretamente')
def insert_examination(context):
    context.driver.find_element_by_id("request_date").click()
    context.driver.find_element_by_xpath("//div[8]/div/table/tbody/tr[3]/td[2]").click()
    context.driver.find_element_by_id("receipt_date").click()
    context.driver.find_element_by_xpath("//div[9]/div/table/tbody/tr[3]/td[2]").click()
    context.driver.find_element_by_id("speciment_collection_date").click()
    context.driver.find_element_by_xpath("//div[10]/div/table/tbody/tr[3]/td[2]").click()
    context.driver.find_element_by_id("received_speciment").clear()
    context.driver.find_element_by_id("received_speciment").send_keys("Material")
    context.driver.find_element_by_id("examination_time").clear()
    context.driver.find_element_by_id("examination_time").send_keys("0000")
    context.driver.find_element_by_id("requesting_physician").clear()
    context.driver.find_element_by_id("requesting_physician").send_keys("Medico")
    context.driver.find_element_by_id("responsible_physician").clear()
    context.driver.find_element_by_id("responsible_physician").send_keys("Responsavel")


@when(u'clica em cadastrar')
def registration(context):
    context.driver.find_element_by_xpath("//input[@value='Enviar']").click()


@then(u'o sistema cadastra o exame e retorna uma mensagem "{message}')
def registration_examitation(context, message):
    success_message = context.driver.find_element_by_xpath("//p[@class='lead']").text

    context.driver.close()
    success_message | should | equal_to(message)



@when(u'o auxiliar digita somente alguns campos obrigatorios')
def insert_examination(context):
    assert False


@then(u'o sistema nao cadastra o exame')
def registration_examitation_fail(context):
    assert False


@when(u'o auxiliar digita algum campo incorretamente')
def insert_examination(context):
    assert False
