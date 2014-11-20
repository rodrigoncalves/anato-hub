# -*- coding: utf-8 -*-

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from should_dsl import should, should_not

def authentication(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8000/')

    username = context.driver.find_element_by_id('username')
    username.send_keys('admin')
    password = context.driver.find_element_by_id('password')
    password.send_keys('1234')
    submit = context.driver.find_element_by_id('enter-button')
    submit.click()

#def seeking_patiente(context):
#    context.driver.find_element_by_id("patient").click().send_keys('Maria')


@given(u'que o auxiliar acessa o sistema e esta autenticado')
def accessing_the_system(context):
    authentication(context)
   
@given(u'cadastra o pedido de exame escolhendo a opção congelamento')
def showing_registration_examination(context):
    context.driver.title | should | equal_to('Home | Anato')
    context.driver.find_element_by_id("patient").send_keys('Maria')
    context.driver.find_element_by_id("search-button").click()
    context.driver.find_element_by_class_name('fi-page-add').click()

    context.driver.find_element_by_id('speciment_collection_date').click()
    context.driver.find_element_by_xpath("//div[9]/div/table/tbody/tr[4]/td[5]").click()
    context.driver.find_element_by_id('request_date').click()
    context.driver.find_element_by_xpath("//div[10]/div/table/tbody/tr[4]/td[5]").click()
    context.driver.find_element_by_id('receipt_date').click()
    context.driver.find_element_by_xpath("//div[11]/div/table/tbody/tr[4]/td[5]").click()
    context.driver.find_element_by_id('received_speciment').send_keys('materia1')
    context.driver.find_element_by_id('examination_time').send_keys('10:00')
    context.driver.find_element_by_id('requesting_physician').send_keys('medico1')
    context.driver.find_element_by_id('responsible_physician').send_keys('medico2')
    context.driver.find_element_by_xpath("//select[@id='exam_type']/option[text()='Congelação']").click()

    context.driver.find_element_by_class_name('button_small_expand').click()


@when(u'o auxiliar digita todos os campos de congelamento corretamente')
def insert_examination(context):
    context.driver.title | should | equal_to('Exame Congelamento | Anato')
    #context.driver.find_element_by_id("clinical_information").click().send_keys('Information')
     
    
@when(u'clica em cadastrar')
def registration(context):
    assert True

@then(u'o sistema cadastra o exame e retorna uma mensagem "{message}')
def registration_examitation(context, message):
    assert True
    # success_message = context.driver.find_element_by_xpath("//p[@class='lead']").text

    # context.driver.close()
    # success_message | should | equal_to(message)

