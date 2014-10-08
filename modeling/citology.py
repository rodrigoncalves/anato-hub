# -*- coding: utf-8 -*-

from django.db import models
from modeling.exam import Exam
from modeling.report import ReportStatus


class CitologyStatus(models.Model):
    description = models.CharField(max_length=50)


class CitologyType(models.Model):
    description = models.CharField(max_length=50)


class SpecimentType(models.Model):
    description = models.CharField(max_length=50)


class Citology(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    macroscopic = models.TextField(null=True, blank=True)
    microscopic = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(CitologyStatus)
    citology_type = models.ForeignKey(CitologyType)
    speciment_type = models.ForeignKey(SpecimentType)
    exam = models.ForeignKey(Exam)


class CitologyReport(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    macroscopic = models.TextField(null=True, blank=True)
    microscopic = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    status = models.ForeignKey(ReportStatus)
    citology_type = models.ForeignKey(CitologyType)
    speciment_type = models.ForeignKey(SpecimentType)
    citology = models.ForeignKey(Citology)
