# -*- coding: utf-8 -*-

import datetime
from django.test import TestCase, Client
from should_dsl import should
from sys import stderr
from core.tests.db_mock import DatabaseMock
from biopsy.models import Cytology
from south.utils import datetime_utils as datetime
from core.tests.format_test import FormatTest


class TestViews(FormatTest, TestCase):
    def setUp(self):
        self.my_type = '[Cytology - Views]'
        stderr.write(self.__str__())
        self.db_mock = DatabaseMock()
        self.db_mock.create_user()
        self.db_mock.create_patient()
        self.db_mock.create_exam_type()
        self.db_mock.create_cytology_status()
        self.db_mock.create_exam_cytology()
        self.db_mock.create_cytology(1)
        self.client = Client()
        self.client.login(username='test_user', password='123456')


    def test_register_biopsy(self):
        response = self.client.post('/citologia/', {
            'cytology_id': '1',
            'examination_time': '12:00',
            'clinical_information': 'teste exame de biopsia',
            'quantity': 'Quantidade',
            'microscopic': 'Microscopia',
            'conclusion': 'Conclusao',
            'note': 'Anotacao qualquer',
            'footer': 'Legenda qualquer'
        })

        cytology_registered = Cytology.objects.get(clinical_information="teste exame de citologia")
        cytology_registered.examination_time | should | equal_to(datetime.time(12, 0))
        cytology_registered.clinical_information | should | equal_to('teste exame de biopsia')
        cytology_registered.quantity | should | equal_to('Quantidade')
        cytology_registered.microscopic | should | equal_to('Microscopia')
        cytology_registered.conclusion | should | equal_to('Conclusao')
        cytology_registered.note | should | equal_to('Anotacao qualquer')
        cytology_registered.footer | should | equal_to('Legenda qualquer')

        # If the method is executed sucessfully, the final instruction is to redirect
        # Status code 302 means sucessfully redirected
        response.status_code | should | equal_to(302)
