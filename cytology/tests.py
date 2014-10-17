# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import models
from cytology.models import Cytology

class CytologyTest(TestCase):

	def cytology_test(self):
		cytology = Cytology(
			clinical_information = "clinica",
			quantity = "quantidade",
			microscopic = "miscroscopia",
			conclusion = "conclusao",
			note = "nota",
			footer = "legenda"
		)

		cytology.save()

		self.assertEquals("clinica", cytology.clinical_information)
		self.assertEquals("quantidade", cytology.quantity)
		self.assertEquals("miscroscopia", cytology.microscopic)
		self.assertEquals("conclusao", cytology.conclusion)
		self.assertEquals("nota", cytology.notes)
		self.assertEquals("legenda", cytology.footer)