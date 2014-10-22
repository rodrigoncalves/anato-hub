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
			footer = "legenda",
			status = "status",
			exam = "exame"
		)

		cytology.save()

		self.assertEquals("clinica", cytology.clinical_information)
		self.assertEquals("quantidade", cytology.quantity)
		self.assertEquals("miscroscopia", cytology.microscopic)
		self.assertEquals("conclusao", cytology.conclusion)
		self.assertEquals("nota", cytology.notes)
		self.assertEquals("legenda", cytology.footer)
		self.assertEquals("status", cytology.status)
		self.assertEquals("exame", cytology.exam)

class CytologyReportTest(TestCase):

	def cytology_report_test(self):
		cytology_report = CytologyReport(
			clinical_information = "clinica",
			quantity = "quantidade",
			microscopic = "miscroscopia",
			conclusion = "conclusao",
			note = "nota",
			footer = "legenda",
			status = "status",
			citology = "citologia"
		)

		cytologyReport.save()

		self.assertEquals("clinica", cytology_report.clinical_information)
		self.assertEquals("quantidade", cytology_report.quantity)
		self.assertEquals("miscroscopia", cytology_report.microscopic)
		self.assertEquals("conclusao", cytology_report.conclusion)
		self.assertEquals("nota", cytology_report.notes)
		self.assertEquals("legenda", cytology_report.footer)
		self.assertEquals("status", cytology_report.status)
		self.assertEquals("citologia", cytology_report.cytology)

