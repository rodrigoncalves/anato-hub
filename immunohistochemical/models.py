# -*- coding: utf-8 -*-
from django.db import models
from exam.models import Exam, ReportStatus


class ImmunoHistochemicalStatus(models.Model):
    description = models.CharField(max_length=50)


class ImmunoHistochemical(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    previous_biopsy = models.CharField(max_length=50, null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(ImmunoHistochemicalStatus)
    exam = models.ForeignKey(Exam)


class AntibodiesTable(models.Model):
    antibody = models.CharField(max_length=100)
    clone = models.CharField(max_length=100)
    result = models.CharField(max_length=255)
    immunohistochemical = models.ForeignKey(ImmunoHistochemical)


class ImmunoHistochemicalReport(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    previous_biopsy = models.CharField(max_length=50, null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    status = models.ForeignKey(ReportStatus)
    immunohistochemical = models.ForeignKey(ImmunoHistochemical)
