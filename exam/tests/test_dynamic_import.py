# -*- coding: utf-8 -*-

from django.test import TestCase
from should_dsl import should
from exam.dynamic_import import create_specific_exam


class TestDynamicImport(TestCase):

    def test_create_biopsy_exam(self):
        from biopsy.models import Biopsy

        specific_exam = create_specific_exam('Biopsy')

        specific_exam | should | be_kind_of(Biopsy)

    def test_create_necropsy_exam(self):
        from necropsy.models import Necropsy

        specific_exam = create_specific_exam('Necropsy')

        specific_exam | should | be_kind_of(Necropsy)

