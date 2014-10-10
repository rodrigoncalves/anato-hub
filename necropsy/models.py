from django.db import models

# Create your models here.
class Necropsy (models.Model):
	clinical_information = models.CharField(max_length=200)
	macroscopic = models.CharField(max_length=200)
	microscopic = models.CharField(max_length=200)
	conclusion = models.CharField(max_length=200)
	notes = models.CharField(max_length=200)
	footer = models.CharField(max_length=200)
