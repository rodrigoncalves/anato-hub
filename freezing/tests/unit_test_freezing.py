# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from should_dsl import should
from sys import stderr
from core.tests.db_mock import DatabaseMock
from freezing.models import Freezing
from core.tests.format_test import FormatTest
import datetime

class TestViews(FormatTest, TestCase):
    def setUp(self):
        self.my_type = '[Freezing - Views]'
        stderr.write(self.__str__())
        self.db_mock = DatabaseMock()
        self.db_mock.create_user()
        self.db_mock.create_patient()
        self.db_mock.create_exam_freezing()
        self.client = Client()
        self.client.login(username='admin', password='1234')

    #Setting biopsy with all fields correctly.
    def test_register_freezing(self):
        response = self.client.post('/congelamento/', {'freezing_id':'1', 'examination_time': '10:00',
        	'clinical_information': 'Informacao', 'macroscopic': 'Macroscopia', 
        	'microscopic': 'Microscopia', 'conclusion': 'Conclusao', 'note': 'Anotacao', 
        	'footer': 'Legenda'})

        freezing_exam = Freezing.objects.get(clinical_information="Informacao")

        freezing_exam.examination_time | should | equal_to(datetime.time(10,0))
        freezing_exam.clinical_information | should | equal_to('Informacao')
        freezing_exam.macroscopic | should | equal_to('Macroscopia')
        freezing_exam.microscopic | should | equal_to('Microscopia')
        freezing_exam.conclusion | should | equal_to('Conclusao')
        freezing_exam.note | should | equal_to('Anotacao')
        freezing_exam.footer | should | equal_to('Legenda')
        #If the method is executed sucessfully, the final instruction is to redirect. Status code 302 means     sucessfully redirected.        
        response.status_code | should | equal_to(302)