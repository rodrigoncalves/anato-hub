# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from should_dsl import should, should_not

from exam.models import ExamType
from core.tests.format_test import FormatTest
from sys import stderr
from core.tests.db_mock import DatabaseMock


class TestViews(FormatTest, TestCase):

    def setUp(self):
        self.my_type = '[Exam - Views]'
        stderr.write(self.__str__())

        mock = DatabaseMock()
        mock.create_biopsy_status()
        mock.create_necropsy_status()
        mock.create_exam_type()
        mock.create_user()
        mock.create_patient()

        self.client = Client()

    def tearDown(self):
        ExamType.objects.all().delete()

    def test_new_exam(self):
        response = self.client.post('/exame/novo/', {
            'patient_id': 1
        })
        # exam_types = list(response.context[-1]['exam_types'])

        response.status_code | should | be(20)
        # exam_types | should_not | be_empty
        # exam_types | should | have(2).heterogeneous_things

    def test_register_exam(self):
        from exam.models import Exam
        before_save_exam = list(Exam.objects.all())

        response = self.client.post('/exame/registrar/', {
            'receipt_date': '01/01/2000',
            'examination_time': '00:00',
            'request_date': '01/01/2000',
            'speciment_collection_date': '01/01/2000',
            'requesting_physician': 'Requesting Physician',
            'received_speciment': 'Received Speciment',
            'csrfmiddlewaretoken': 'csrf_token',
            'responsible_physician': 'Responsible Pyshician',
            'exam_type': '1',
        })

        after_save_exam = list(Exam.objects.all())

        # response.status_code | should | be(200)
        # len(after_save_exam) | should | be_greater_than(len(before_save_exam))

    def test_register_new_biopsy(self):
        from biopsy.models import Biopsy
        before_create_biopsy = list(Biopsy.objects.all())

        response = self.client.post('/exame/registrar/', {
            'receipt_date': '01/01/2000',
            'examination_time': '00:00',
            'request_date': '01/01/2000',
            'speciment_collection_date': '01/01/2000',
            'requesting_physician': 'Requesting Physician',
            'received_speciment': 'Received Speciment',
            'csrfmiddlewaretoken': 'csrf_token',
            'responsible_physician': 'Responsible Pyshician',
            'exam_type': '1',
        })

        after_create_biopsy = list(Biopsy.objects.all())

        # response.status_code | should | be(200)
        # len(after_create_biopsy) | should | be_greater_than(
        # len(before_create_biopsy))

    def test_register_new_necropsy(self):
        from necropsy.models import Necropsy
        before_create_necropsy = list(Necropsy.objects.all())

        response = self.client.post('/exame/registrar/', {
            'receipt_date': '01/01/2000',
            'examination_time': '00:00',
            'request_date': '01/01/2000',
            'speciment_collection_date': '01/01/2000',
            'requesting_physician': 'Requesting Physician',
            'received_speciment': 'Received Speciment',
            'csrfmiddlewaretoken': 'csrf_token',
            'responsible_physician': 'Responsible Pyshician',
            'exam_type': '2',
        })

        after_create_necropsy = list(Necropsy.objects.all())

        # response.status_code | should | be(200)
        # len(after_create_necropsy) | should | be_greater_than(
        # len(before_create_necropsy))
