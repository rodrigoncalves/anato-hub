# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import models
from models import Immunohistochemical

class ImmunohistochemicalTest(TestCase):

	def test_immunohistochemical(self):

		immunohistochemical = Immunohistochemical(
			clinical_information= "clinica",
			previous_biopsy = "biopsia anterior",
			conclusion  = "conclusao",
			note = "nota",
			footer= "legenda"
		)

		self.assertEquals("clinica",immunohistochemical.clinical_information)
		self.assertEquals("biopsia anterior",immunohistochemical.previous_biopsy)
		self.assertEquals("conclusao",immunohistochemical.conclusion)
		self.assertEquals("nota",immunohistochemical.note)
		self.assertEquals("legenda",immunohistochemical.footer)
