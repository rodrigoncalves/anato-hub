# -*- coding: utf-8 -*-
from selenium import webdriver


def authentication(context):
    context.driver = webdriver.Firefox()
    context.driver.get('http://localhost:8000/')

    username = context.driver.find_element_by_id('username')
    username.send_keys('larissa')
    password = context.driver.find_element_by_id('password')
    password.send_keys('1234')
    submit = context.driver.find_element_by_id('enter-button')
    submit.click()
