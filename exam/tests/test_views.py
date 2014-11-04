# -*- coding: utf-8 -*-

from django.test import TestCase, Client
from should_dsl import should, should_not

from core.tests.format_test import FormatTest
from sys import stderr
from core.tests.db_mock import DatabaseMock


class TestViews(FormatTest, TestCase):

    
    def setUp(self):
        self.my_type = '[Exam - Views]'
        stderr.write(self.__str__())

        self.mock = DatabaseMock()
        self.mock.create_exam_type()
        self.mock.create_user()

        self.client = Client()
        self.client.login(username='test_user', password='123456')

    
    def test_new_exam(self):
        self.mock.create_patient()
        response = self.client.post('/exame/novo/', {
            'patient_id': '1',
        })
        exam_types = list(response.context[-1]['exam_types'])

        response.status_code | should | be(200)
        exam_types | should_not | be_empty
        exam_types | should | have(4).heterogeneous_things

    
    def test_register_exam(self):
        from exam.models import Exam
        before_save_exam = list(Exam.objects.all())

        self.mock.create_biopsy_status()
        response = self.client.post('/exame/registrar/', {
            'patient_id': '1',
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

        response.status_code | should | be(200)
        len(after_save_exam) | should | be_greater_than(len(before_save_exam))

    
    def test_register_new_biopsy(self):
        from biopsy.models import Biopsy
        before_create_biopsy = list(Biopsy.objects.all())

        self.mock.create_biopsy_status()
        response = self.client.post('/exame/registrar/', {
            'patient_id': '1',
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

        response.status_code | should | be(200)
        len(after_create_biopsy) | should | be_greater_than(
            len(before_create_biopsy))

    
    def test_register_new_necropsy(self):
        from necropsy.models import Necropsy
        before_create_necropsy = list(Necropsy.objects.all())

        self.mock.create_necropsy_status()
        response = self.client.post('/exame/registrar/', {
            'patient_id': '1',
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

        response.status_code | should | be(200)
        len(after_create_necropsy) | should | be_greater_than(
            len(before_create_necropsy))

    
    def test_register_new_immunohistochemical(self):
        from immunohistochemical.models import ImmunoHistochemical
        before_create_immunohistochemical = list(
            ImmunoHistochemical.objects.all())

        self.mock.create_immunohistochemical_status()
        response = self.client.post('/exame/registrar/', {
            'patient_id': '1',
            'receipt_date': '01/01/2000',
            'examination_time': '00:00',
            'request_date': '01/01/2000',
            'speciment_collection_date': '01/01/2000',
            'requesting_physician': 'Requesting Physician',
            'received_speciment': 'Received Speciment',
            'csrfmiddlewaretoken': 'csrf_token',
            'responsible_physician': 'Responsible Pyshician',
            'exam_type': '3',
        })

        after_create_immunohistochemical = list(
            ImmunoHistochemical.objects.all())

        response.status_code | should | be(200)
        len(after_create_immunohistochemical) | should | be_greater_than(
            len(before_create_immunohistochemical))

    
    def test_register_new_cytology(self):
        from cytology.models import Cytology
        before_create_cytology = list(
            Cytology.objects.all())

        self.mock.create_cytology_status
        response = self.client.post('/exame/registrar/', {
            'patient_id': '1',
            'receipt_date': '01/01/2000',
            'examination_time': '00:00',
            'request_date': '01/01/2000',
            'speciment_collection_date': '01/01/2000',
            'requesting_physician': 'Requesting Physician',
            'received_speciment': 'Received Speciment',
            'csrfmiddlewaretoken': 'csrf_token',
            'responsible_physician': 'Responsible Pyshician',
            'exam_type': '4',
        })

        after_create_cytology = list(
            Cytology.objects.all())

        response.status_code | should | be(200)
        len(after_create_cytology) | should | be_greater_than(
            len(before_create_cytology))
