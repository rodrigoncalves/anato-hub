# -*- coding: utf-8 -*-
from django.db import models
from exam.models import Exam, ReportStatus


class ImmunoHistochemicalStatus(models.Model):
    description = models.CharField(max_length=50)


class ImmunoHistochemical(models.Model):

    def exam_antibodies(self):
        return AntibodiesTable.objects.filter(immunohistochemical=self.id)

    clinical_information = models.TextField(null=True, blank=True)
    previous_biopsy = models.CharField(max_length=50, null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    status = models.ForeignKey(ImmunoHistochemicalStatus, default=1)
    exam = models.ForeignKey(Exam)
    antibodies = property(exam_antibodies)


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
