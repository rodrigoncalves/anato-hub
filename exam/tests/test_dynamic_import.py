# -*- coding: utf-8 -*-

from django.test import TestCase
from should_dsl import should

from exam.dynamic_import import create_specific_exam
from core.tests import FormatTest
from sys import stderr


class TestDynamicImport(FormatTest, TestCase):

    def setUp(self):
        self.my_type = '[Exam - Dynamic Import]'
        stderr.write(self.__str__())

    def test_create_biopsy_exam(self):
        from biopsy.models import Biopsy

        biopsy_exam = create_specific_exam('Biopsy')

        biopsy_exam | should | be_kind_of(Biopsy)

    def test_create_necropsy_exam(self):
        from necropsy.models import Necropsy

        necropsy_exam = create_specific_exam('Necropsy')

        necropsy_exam | should | be_kind_of(Necropsy)

    def test_create_specific_exam_invalid_param(self):
        from exam.exceptions import InvalidParameter

        InvalidParameter | should | be_thrown_by(lambda: create_specific_exam(
            ''))

    def test_create_specific_exam_invalid_model(self):
        from exam.exceptions import ModelDoesNotExist

        ModelDoesNotExist | should | be_thrown_by(lambda: create_specific_exam(
            'InvalidModel'))
