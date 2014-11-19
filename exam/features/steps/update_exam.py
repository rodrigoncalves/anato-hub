# -*- coding: utf-8 -*-
from behave import given, when, then
from selenium import webdriver
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


@given(u'que o usuario esta autenticado')
def authenticate(context):
    authentication(context)
	

@given(u'que o usuario esta na tela de informacoes do exame')
def display_informations(context):
	context.driver.get("http://localhost:8000/paciente/36063")
	context.verificationErrors = []
	context.accept_next_alert = True
	driver = context.driver
	driver.find_element_by_css_selector("dd > a").click()
	context.driver.get("http://localhost:8000/exame/5")

@when(u'o usuario clica em editar')
def click_edit_button(context):
	driver = context.driver
	context.driver.get("http://localhost:8000/exame/atualizar/5")

@when(u'atualiza todos os campos')
def update_fields(context):
	context.driver.find_element_by_id("received_speciment").clear()
	context.driver.find_element_by_id("received_speciment").send_keys("Material")
	context.driver.find_element_by_id("examination_time").clear()
	context.driver.find_element_by_id("examination_time").send_keys("0000")
	context.driver.find_element_by_id("requesting_physician").clear()
	context.driver.find_element_by_id("requesting_physician").send_keys("Medico")
	context.driver.find_element_by_id("responsible_physician").clear()
	context.driver.find_element_by_id("responsible_physician").send_keys("Responsavel")

@when(u'clica no botao atualizar')
def click_update_button(context):
	driver = context.driver
	driver.find_element_by_xpath("//input[@value='Atualizar']").click()

@then(u'o sistema apresenta a tela de informacoes do exame')
def step_impl(context):
	context.driver.title | should | equal_to('Visualizar Exame | Anato')

@when(u'atualiza todos os campos e deixa o material recebido em branco')
def update_all_less_material(context):
	context.driver.find_element_by_id("received_speciment").clear()
	context.driver.find_element_by_id("examination_time").clear()
	context.driver.find_element_by_id("examination_time").send_keys("0000")
	context.driver.find_element_by_id("requesting_physician").clear()
	context.driver.find_element_by_id("requesting_physician").send_keys("Medico")
	context.driver.find_element_by_id("responsible_physician").clear()
	context.driver.find_element_by_id("responsible_physician").send_keys("Responsavel")

@then(u'o sistema apresenta uma mensagem de erro e nao volta pra tela de informacoes do exame')
def step_impl(context):
	context.driver.title | should | equal_to('Atualizar Exame | Anato HUB')


@when(u'atualiza todos os campos e deixa a hora do exame em branco')
def update_all_less_examination_time(context):
	context.driver.find_element_by_id("received_speciment").clear()
	context.driver.find_element_by_id("received_speciment").send_keys("Material")
	context.driver.find_element_by_id("examination_time").clear()
	context.driver.find_element_by_id("requesting_physician").clear()
	context.driver.find_element_by_id("requesting_physician").send_keys("Medico")
	context.driver.find_element_by_id("responsible_physician").clear()
	context.driver.find_element_by_id("responsible_physician").send_keys("Responsavel")

@when(u'atualiza todos os campos e deixa o medico requisitante em branco')
def update_all_less_requesting_physician(context):
	context.driver.find_element_by_id("received_speciment").clear()
	context.driver.find_element_by_id("received_speciment").send_keys("Material")
	context.driver.find_element_by_id("examination_time").clear()
	context.driver.find_element_by_id("examination_time").send_keys("0000")
	context.driver.find_element_by_id("requesting_physician").clear()
	context.driver.find_element_by_id("responsible_physician").clear()
	context.driver.find_element_by_id("responsible_physician").send_keys("Responsavel")

@when(u'atualiza todos os campos e deixa o medico responsavel em branco')
def update_all_less_requesting_physician(context):
	context.driver.find_element_by_id("received_speciment").clear()
	context.driver.find_element_by_id("received_speciment").send_keys("Material")
	context.driver.find_element_by_id("examination_time").clear()
	context.driver.find_element_by_id("examination_time").send_keys("0000")
	context.driver.find_element_by_id("requesting_physician").clear()
	context.driver.find_element_by_id("requesting_physician").send_keys("Medico")
	context.driver.find_element_by_id("responsible_physician").clear()
