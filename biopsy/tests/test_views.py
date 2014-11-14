# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from should_dsl import should
from sys import stderr
from core.tests.db_mock import DatabaseMock
from biopsy.models import Biopsy

class TestViews(TestCase):
    def setUp(self):
        self.my_type = '[Biopsy - Views]'
        stderr.write(self.__str__())
        self.db_mock = DatabaseMock()
        self.db_mock.create_user()
        self.db_mock.create_patient()
        self.db_mock.create_exam_biopsy()
        self.db_mock.create_biopsy(1)
        self.client = Client()
        self.client.login(username='test_user', password='123456')

    #Setting biopsy with all fields correctly.
    def test_register_biopsy(self):
        response = self.client.post('/biopsia/', {'biopsy_id':'1', 'clinical_information': 'teste exame de biopsia', 'macroscopic': 'Macroscopia', 'microscopic': 'Microscopia', 'conclusion': 'Conclusao', 'note': 'Anotacao qualquer', 'footer': 'Legenda qualquer'})
        biopsy_registered = Biopsy.objects.get(clinical_information="teste exame de biopsia")

        biopsy_registered.clinical_information | should | equal_to('teste exame de biopsia')
        biopsy_registered.macroscopic | should | equal_to('Macroscopia')
        biopsy_registered.microscopic | should | equal_to('Microscopia')
        biopsy_registered.conclusion | should | equal_to('Conclusao')
        biopsy_registered.note | should | equal_to('Anotacao qualquer')
        biopsy_registered.footer | should | equal_to('Legenda qualquer')
        #If the method is executed sucessfully, the final instruction is to redirect. Status code 302 means     sucessfully redirected.        
        response.status_code | should| equal_to(302)
