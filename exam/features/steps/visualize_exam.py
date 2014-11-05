# -*- coding: utf-8 -*-

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from should_dsl import should, should_not
from core.tests.db_mock import DatabaseMock

def authentication(context):
	context.driver = webdriver.Firefox()
	context.driver.get('http://localhost:8000/')

	username = context.driver.find_element_by_id('username')
	username.send_keys('ana')
	password = context.driver.find_element_by_id('password')
	password.send_keys('root')
	submit = context.driver.find_element_by_id('enter-button')
	submit.click()

@given(u'que o usuario acessa o perfil do paciente')
def accessing_patient_profile(context):
	authentication(context)
	context.driver = webdriver.Firefox()
	context.driver.implicitly_wait(30)
	context.driver.get("http://127.0.0.1:8000/paciente/36063")
	context.verificationErrors = []
	context.accept_next_alert = True

@when(u'ele clica no exame desejado')
def step_impl(context):
    driver = context.driver
    driver.find_element_by_css_selector("dd > a").click()

@when(u'clica em Ver Exame')
def visualize(context):
    context.driver.find_element_by_xpath("//div[@id='exam2']/div/div[2]/form/button").click()

@then(u'o sistema exibe o exame completo do paciente')
def step_impl(context):
    assert False
