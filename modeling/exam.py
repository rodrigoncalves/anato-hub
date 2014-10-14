# -*- coding: utf-8 -*-

from django.db import models


class Exam(models.Model):
    request_date = models.DateField()
    receipt_date = models.DateField()
    speciment_collection_date = models.DateField()
    received_speciment = models.CharField(max_length=50, null=True, blank=True)
    examination_time = models.TimeField()
    requesting_physician = models.CharField(max_length=50)
    responsible_physician = models.CharField(max_length=50)
