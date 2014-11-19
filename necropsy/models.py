# -*- coding: utf-8 -*-

from django.db import models
from exam.models import Exam, ReportStatus


class NecropsyStatus(models.Model):
    description = models.CharField(max_length=50)


class Necropsy(models.Model):
    examination_time = models.TimeField(null=True, blank=True)
    clinical_information = models.TextField(null=True, blank=True)
    main_disease = models.TextField(null=True, blank=True)
    consequential_final_disease = models.TextField(null=True, blank=True)
    contributors_disease = models.TextField(null=True, blank=True)
    consequential_disease = models.TextField(null=True, blank=True)
    other_diseases = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(NecropsyStatus, default=1)
    exam = models.ForeignKey(Exam)


class NecropsyReport(models.Model):
    clinical_information = models.TextField(null=True, blank=True)
    main_disease = models.TextField(null=True, blank=True)
    consequential_final_disease = models.TextField(null=True, blank=True)
    contributors_disease = models.TextField(null=True, blank=True)
    consequential_disease = models.TextField(null=True, blank=True)
    other_diseases = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(ReportStatus, default=1)
    necropsy = models.ForeignKey(Necropsy)
