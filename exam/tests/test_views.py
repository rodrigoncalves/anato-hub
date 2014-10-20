# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from should_dsl import should, should_not


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_new_exam(self):
        from exam.models import ExamType
        ExamType.objects.create(description='Biópsia', name_class='Biopsy')
        ExamType.objects.create(description='Necrópsia', name_class='Necropsy')

        response = self.client.get('/exame/novo/')
        exam_types = list(response.context[-1]['exam_types'])

        response.status_code | should | be(200)
        exam_types | should_not | be_empty
        exam_types | should | have(2).heterogeneous_things
