# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Necropsy (models.Model):
	clinical_information = models.TextField(null=True, blank=True)
	macroscopic = models.TextField(null=True, blank=True)
	microscopic = models.TextField(null=True, blank=True)
	conclusion = models.TextField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	footer = models.TextField(null=True, blank=True)

