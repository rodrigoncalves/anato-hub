from django.db import models

class ProfileType(models.Model):
	description = models.CharField(max_length=50)
