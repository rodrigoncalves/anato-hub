# -*- coding: utf-8 -*-

from django.db import models
from exam.models import Exam
from modeling.report import ReportStatus


class BiopsyStatus(models.Model):
    description = models.CharField(max_length=50)


class Biopsy(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    macroscopic = models.TextField(null=True, blank=True)
    microscopic = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(BiopsyStatus)
    exam = models.ForeignKey(Exam)


class BiopsyReport(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    macroscopic = models.TextField(null=True, blank=True)
    microscopic = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    status = models.ForeignKey(ReportStatus)
    biopsy = models.ForeignKey(Biopsy)
