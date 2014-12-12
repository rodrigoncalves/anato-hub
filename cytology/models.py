# -*- conding: utf-8 -*-

from django.db import models
from exam.models import Exam, ReportStatus


class CytologyStatus(models.Model):
    description = models.CharField(max_length=50)


class Cytology(models.Model):
    examination_time = models.TimeField(
        null=True, blank=True)
    clinical_information = models.TextField(
        null=True, blank=True)
    quantity = models.TextField(
        null=True, blank=True)
    microscopic = models.TextField(
        null=True, blank=True)
    conclusion = models.TextField(
        null=True, blank=True)
    note = models.TextField(
        null=True, blank=True)
    footer = models.TextField(
        null=True, blank=True)
    status = models.ForeignKey(CytologyStatus, default=1)
    exam = models.ForeignKey(Exam)


class CytologyReport(models.Model):
    examination_time = models.TimeField(
        null=True, blank=True)
    clinical_information = models.CharField(
        max_length=255, null=True, blank=True)
    quantity = models.CharField(
        max_length=255, null=True, blank=True)
    microscopic = models.CharField(
        max_length=255, null=True, blank=True)
    conclusion = models.CharField(
        max_length=255, null=True, blank=True)
    note = models.CharField(
        max_length=255, null=True, blank=True)
    footer = models.CharField(
        max_length=255, null=True, blank=True)
    status = models.ForeignKey(ReportStatus, default=1)
    cytology = models.ForeignKey(Cytology)
