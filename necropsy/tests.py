# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import models
from necropsy.models import Necropsy

class NecropsyTest(TestCase):

	def necropsy_test(self):
		necropsy = Necropsy(
			clinical_information= "clinica",
			macroscopic= "macroscopia",
			microscopic= "microscopia",
			conclusion= "conclusao",
			notes= "nota",
			footer= "rodape"
		)

		necropsy.save()

		self.assertEquals("clinica",necropsy.clinical_information)
		self.assertEquals("macroscopia",necropsy.macroscopic)
		self.assertEquals("microscopia",necropsy.microscopic)
		self.assertEquals("conclusao",necropsy.conclusion)
		self.assertEquals("nota",necropsy.notes)
		self.assertEquals("rodape",necropsy.footer)