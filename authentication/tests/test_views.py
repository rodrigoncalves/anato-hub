# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from should_dsl import should
from core.tests.format_test import FormatTest
from sys import stderr
from core.tests.db_mock import DatabaseMock
import re #Regular expressions

class TestViews(FormatTest, TestCase):
    
    def setUp(self):
        self.my_type = '[Authentication - Views]'
        stderr.write(self.__str__())
        
        self.mock = DatabaseMock()
        self.mock.create_user()
        self.client = Client()

    def test_log_out(self):
        self.client.post('/', {'username': 'test_user', 'password': '123456'})
        response = self.client.get('/sair/')
        response.status_code | should | equal_to(302)

    #User inactive needs to be implemented.
    #User LDAP authentication error needs to be implemented.
    def test_sign_in(self):
        #User not authenticated.
        template_in_response = False
        response = self.client.get('/')
        response.status_code | should | equal_to(200)
        for i in range(0, len(response.templates)):
            #Search for template 'sign_in.html' in response object.
            if response.templates[i].name == 'sign_in.html':
                template_in_response = True
                break
        template_in_response | should | equal_to(True)

        #User authenticating. Sucessfully redirected.
        response = self.client.post('/', {'username': 'test_user', 'password': '123456'})
        response.status_code | should | equal_to(302)
        #User authenticating. Failed authentication, invalid login.
        self.client.get('/sair/')
        response = self.client.post('/', {'username': 'invalid_user', 'password': 'invalid'})
        response.status_code | should | equal_to(200)
        response.content | should | be_like(r'.*Nome de usuário ou senha incorretos\..*', re.S)




