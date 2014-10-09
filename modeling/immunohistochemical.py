# -*- coding: utf-8 -*-

from django.db import models
from modeling.exam import Exam
from modeling.report import ReportStatus


class ImmunohistochemicalStatus(models.Model):
    description = models.CharField(max_length=50)


class Immunohistochemical(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    previous_biopsy = models.CharField(max_length=50, null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(ImmunohistochemicalStatus)
    exam = models.ForeignKey(Exam)


class AntibodiesTable(models.Model):
    antibody = models.CharField(max_length=100)
    clone = models.CharField(max_length=100)
    result = models.CharField(max_length=255)
    immunohistochemical = models.ManyToManyField(Immunohistochemical)


class ImmunohistochemicalReport(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    previous_biopsy = models.CharField(max_length=50, null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    status = models.ForeignKey(ReportStatus)
    immunohistochemical = models.ForeignKey(Immunohistochemical)
