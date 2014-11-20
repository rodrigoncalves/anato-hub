# -*- coding: utf-8 -*-

from django.test import TestCase
from should_dsl import should
from sys import stderr
from core.tests.format_test import FormatTest
from core.tests.db_mock import DatabaseMock


class TestModels(FormatTest, TestCase):

    def setUp(self):
        self.my_type = '[Exam - Models]'
        stderr.write(self.__str__())
        self.mock = DatabaseMock()

    def test_property_specific_exam(self):
        from exam.models import Exam
        from biopsy.models import Biopsy

        self.mock.create_exam_type()
        self.mock.create_exam_biopsy()
        exam = Exam.objects.earliest('id')

        exam.specific_exam | should | be_kind_of(Biopsy)

    def test_property_patient_information(self):
        from exam.models import Exam
        from patients.models import Paciente

        self.mock.create_patient()
        self.mock.create_exam_biopsy()
        exam = Exam.objects.get(id=1)

        exam.patient_information | should | be_kind_of(Paciente)
