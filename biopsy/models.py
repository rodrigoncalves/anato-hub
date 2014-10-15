# -*- coding: utf-8 -*-
from django.db import models
from exam.models import Exam, ReportStatus


class BiopsyStatus(models.Model):
    description = models.CharField(max_length=50)


class Biopsy(models.Model):
    clinical_information = models.CharField(
        max_length=255, null=True, blank=True)
    macroscopic = models.CharField(
        max_length=255, null=True, blank=True)
    microscopic = models.CharField(
        max_length=255, null=True, blank=True)
    conclusion = models.CharField(
        max_length=255, null=True, blank=True)
    note = models.CharField(
        max_length=255, null=True, blank=True)
    footer = models.CharField(
        max_length=255, null=True, blank=True)
    status = models.ForeignKey(BiopsyStatus, default=1)
    exam = models.ForeignKey(Exam)


class BiopsyReport(models.Model):
    clinical_information = models.CharField(
        max_length=255, null=True, blank=True)
    macroscopic = models.CharField(
        max_length=255, null=True, blank=True)
    microscopic = models.CharField(
        max_length=255, null=True, blank=True)
    conclusion = models.CharField(
        max_length=255, null=True, blank=True)
    note = models.CharField(
        max_length=255, null=True, blank=True)
    status = models.ForeignKey(ReportStatus)
    biopsy = models.ForeignKey(Biopsy)
