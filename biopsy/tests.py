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


class BiopsyReportTest(TestCase):

	def biopy_report_test(self):
		biopsy_report = BiopsyReport(
			clinical_information= "clinica",
			macroscopic= "macroscopia",
			microscopic= "microscopia",
			conclusion= "conclusao",
			notes= "nota",
			status = "status",
			exam = "exame",
			biopsy = "biopsia"
		)

		biopsy_report.save()

		self.assertEquals("clinica",biopsy_report.clinical_information)
		self.assertEquals("macroscopia",biopsy_report.macroscopic)
		self.assertEquals("microscopia",biopsy_report.microscopic)
		self.assertEquals("conclusao",biopsy_report.conclusion)
		self.assertEquals("nota",biopsy_report.notes)
		self.assertEquals("status",biopsy_report.status)
		self.assertEquals("exameeee",biopsy_report.exam)
		self.assertEquals("biopsia",biopsy_report.biopsy)