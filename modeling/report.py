# -*- coding: utf-8 -*-

from django.db import models


class ReportStatus(models.Model):
    description = models.CharField(max_length=50)
