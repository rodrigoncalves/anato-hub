# -*- coding: utf-8 -*-

from django.db import models
from exam.models import Exam
from modeling.report import ReportStatus


class NecropsyStatus(models.Model):
    description = models.CharField(max_length=50)

class Necropsy(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    main_disease = models.TextField(null=True, blank=True)
    consequential_final_disease = models.TextField(null=True, blank=True)
    contributors_disease = models.TextField(null=True, blank=True)
    consequential_disease = models.TextField(null=True, blank=True)
    other_disases = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(NecropsyStatus)
    exam = models.ForeignKey(Exam)

class NecropsyReport(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    main_disease = models.TextField(null=True, blank=True)
    consequential_final_disease = models.TextField(null=True, blank=True)
    contributors_disease = models.TextField(null=True, blank=True)
    consequential_disease = models.TextField(null=True, blank=True)
    other_disases = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(ReportStatus)
    necropsy = models.ForeignKey(Necropsy)
