# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db import models
#from immunohistochemical import Immunohistochemical

class ImmunohistochemicalTest(TestCase):

	def immunohistochemical_test(self):
		immunohistochemical = Immunohistochemical(
			clinical_information= "clinica",
			previous_biopsy = "previsao",
			conclusion  = "conclusao",
			note = "nota",
			footer= "rodape"
		)

		immunohistochemical.save()

		self.assertEquals("clinica",immunohistochemical.clinical_information)
		self.assertEquals("previsao",immunohistochemical.previous_biopsy)
		self.assertEquals("conclusao",immunohistochemical.conclusion)
		self.assertEquals("nota",immunohistochemical.note)
		self.assertEquals("rodape",immunohistochemical.footer)

		#Verificar se é necessário incluir esses atributos
		#status = models.ForeignKey(ImmunohistochemicalStatus)
		#exam = models.ForeignKey(Exam)