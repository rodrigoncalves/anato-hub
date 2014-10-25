# -*- coding: utf-8 -*-

from django.test import TestCase
from should_dsl import should
from core.tests.format_test import FormatTest
from sys import stderr


class TestModels(FormatTest, TestCase):

    def setUp(self):
        self.my_type = '[Exam - Models]'
        stderr.write(self.__str__())

    # def test_property_specific_exam(self):
