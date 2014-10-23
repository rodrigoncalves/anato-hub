# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import models
from models import Biopsy
from models import BiopsyReport

class BiopsyTest(TestCase):

	def test_biopsy(self):
		biopsy = Biopsy(
			clinical_information= 'clinica',
			macroscopic= 'macroscopia',
			microscopic= 'microscopia',
			conclusion= 'conclusao',
			note = 'nota',
			footer= 'legenda'
		)

		self.assertEquals('clinica',biopsy.clinical_information)
		self.assertEquals('macroscopia',biopsy.macroscopic)
		self.assertEquals('microscopia',biopsy.microscopic)
		self.assertEquals('conclusao',biopsy.conclusion)
		self.assertEquals('nota',biopsy.note)
		self.assertEquals('legenda',biopsy.footer)


class BiopsyReportTest(TestCase):

	def test_biopy_report(self):
		biopsy_report = BiopsyReport(
			clinical_information= "clinica",
			macroscopic= "macroscopia",
			microscopic= "microscopia",
			conclusion= "conclusao",
			note= "nota",
		)

		self.assertEquals("clinica",biopsy_report.clinical_information)
		self.assertEquals("macroscopia",biopsy_report.macroscopic)
		self.assertEquals("microscopia",biopsy_report.microscopic)
		self.assertEquals("conclusao",biopsy_report.conclusion)
		self.assertEquals("nota",biopsy_report.note)
