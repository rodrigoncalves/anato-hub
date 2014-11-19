# -*- coding: utf-8 -*-

from django.db import models

class ExamType(models.Model):

    description = models.CharField(max_length=50)
    name_class = models.CharField(max_length=50)


class Exam(models.Model):

    
    def get_specific_exam(self):
        from core.dynamic_import import import_class
        class_ = import_class(self.exam_type)
        return class_.objects.get(exam=self)

    
    def get_patient_information(self):
        from patients.models import Paciente
        patient = Paciente.objects.using("hub").get(codigo=self.patient)
        return patient


    request_date = models.DateField()
    receipt_date = models.DateField()
    speciment_collection_date = models.DateField()
    received_speciment = models.CharField(max_length=50, null=True, blank=True)
    requesting_physician = models.CharField(max_length=50)
    responsible_physician = models.CharField(max_length=50)
    exam_type = models.ForeignKey(ExamType)
    patient = models.BigIntegerField()
    specific_exam = property(get_specific_exam)
    patient_information = property(get_patient_information)


class ReportStatus(models.Model):
    description = models.CharField(max_length=50)
