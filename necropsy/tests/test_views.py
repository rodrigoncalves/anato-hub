# -*- coding: utf-8 -*-

import datetime
from django.test import TestCase, Client
from should_dsl import should
from sys import stderr
from core.tests.db_mock import DatabaseMock
from necropsy.models import Necropsy
from south.utils import datetime_utils as datetime
from core.tests.format_test import FormatTest


class TestViews(FormatTest, TestCase):
    def setUp(self):
        self.my_type = '[Necropsy - Views]'
        stderr.write(self.__str__())
        self.db_mock = DatabaseMock()
        self.db_mock.create_user()
        self.db_mock.create_patient()
        self.db_mock.create_exam_type()
        self.db_mock.create_necropsy_status()
        self.db_mock.create_exam_necropsy()
        self.db_mock.create_necropsy(1)
        self.client = Client()
        self.client.login(username='test_user', password='123456')


    def test_register_necropsy(self):
        response = self.client.post('/autopsia/', {
            'necropsy_id': '2',
            'examination_time': '12:00',
            'clinical_information': 'teste exame de necropsia',
            'main_disease': 'Doenca Principal',
            'consequential_final_disease': 'Consequencia da Doenca',
            'contributors_disease': 'Doencas Contribuintes',
            'consequential_disease': 'Consequencia da Doenca',
            'other_diseases': 'Outras Doencas',
            'note': 'Nota',
            'footer': 'Legenda'
        })

        necropsy_registered = Necropsy.objects.get(clinical_information='teste exame de necropsia')
        necropsy_registered.examination_time | should | equal_to(datetime.time(12, 0))
        necropsy_registered.clinical_information | should | equal_to('teste exame de necropsia')
        necropsy_registered.main_disease | should | equal_to('Doenca Principal')
        necropsy_registered.consequential_final_disease | should | equal_to('Consequencia da Doenca')
        necropsy_registered.contributors_disease | should | equal_to('Doencas Contribuintes')
        necropsy_registered.consequential_disease | should | equal_to('Consequencia da Doenca')
        necropsy_registered.other_diseases | should | equal_to('Outras Doencas')
        necropsy_registered.note | should | equal_to('Nota')
        necropsy_registered.footer | should | equal_to('Legenda')

        # If the method is executed sucessfully, the final instruction is to render
        # Status code 200 means sucessfully redered
        response.status_code | should | equal_to(302)
