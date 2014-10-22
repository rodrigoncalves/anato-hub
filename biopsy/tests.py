# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import models
from biopsy.models import Biopsy

class BiopsyTest(TestCase):

	def biopy_test(self):
		biopsy = Biopsy(
			clinical_information= "clinica",
			macroscopic= "macroscopia",
			microscopic= "microscopia",
			conclusion= "conclusao",
			notes= "nota",
			footer= "legenda",
			status = "status",
			exam = "exame"
		)

		biopsy.save()

		self.assertEquals("clinica",biopsy.clinical_information)
		self.assertEquals("macroscopia",biopsy.macroscopic)
		self.assertEquals("microscopia",biopsy.microscopic)
		self.assertEquals("conclusao",biopsy.conclusion)
		self.assertEquals("nota",biopsy.notes)
		self.assertEquals("legenda",biopsy.footer)
		self.assertEquals("status",biopsy.status)
		self.assertEquals("exame",biopsy.exam)
