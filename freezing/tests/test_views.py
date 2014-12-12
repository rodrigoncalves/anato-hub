# -*- coding: utf-8 -*-

import datetime
from django.test import TestCase, Client
from should_dsl import should
from sys import stderr
from core.tests.db_mock import DatabaseMock
from freezing.models import Freezing
from south.utils import datetime_utils as datetime
from core.tests.format_test import FormatTest


class TestViews(FormatTest, TestCase):
    def setUp(self):
        self.my_type = '[Freezing - Views]'
        stderr.write(self.__str__())
        self.db_mock = DatabaseMock()
        self.db_mock.create_user()
        self.db_mock.create_patient()
        self.db_mock.create_exam_type()
        self.db_mock.create_freezing_status()
        self.db_mock.create_exam_freezing()
        self.db_mock.create_freezing(1)
        self.client = Client()
        self.client.login(username='test_user', password='123456')


    def test_register_biopsy(self):
        response = self.client.post('/congelamento/', {
            'freezing_id': '1',
            'clinical_information': 'teste exame de congelamento',
            'macroscopic': 'Macroscopia',
            'microscopic': 'Microscopia',
            'conclusion': 'Conclusao',
            'note': 'Anotacao qualquer',
            'footer': 'Legenda qualquer'
        })

        freezing_registered = Freezing.objects.get(clinical_information="teste exame de congelamento")
        freezing_registered.clinical_information | should | equal_to('teste exame de congelamento')
        freezing_registered.macroscopic | should | equal_to('Macroscopia')
        freezing_registered.microscopic | should | equal_to('Microscopia')
        freezing_registered.conclusion | should | equal_to('Conclusao')
        freezing_registered.note | should | equal_to('Anotacao qualquer')
        freezing_registered.footer | should | equal_to('Legenda qualquer')

        # If the method is executed sucessfully, the final instruction is to redirect
        # Status code 302 means sucessfully redirected
        response.status_code | should | equal_to(302)
