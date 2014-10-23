# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import models
from models import Necropsy

class NecropsyTest(TestCase):

	def test_necropsy(self):

		necropsy = Necropsy(
			clinical_information = 'clinica',
			main_disease = 'doenca',
			contributors_disease = 'consequencia',
			consequential_disease = 'consequencia',
			other_disases = 'outra doenca',
			note = 'nota',
			footer = 'rodape'
		)

		self.assertEquals('clinica',necropsy.clinical_information)
		self.assertEquals('doenca',necropsy.main_disease)
		self.assertEquals('consequencia',necropsy.contributors_disease)
		self.assertEquals('consequencia',necropsy.consequential_disease)
		self.assertEquals('outra doenca',necropsy.other_disases)
		self.assertEquals('nota',necropsy.note)
		self.assertEquals('rodape',necropsy.footer)
