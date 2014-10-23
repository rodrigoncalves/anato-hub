from django.db import models

# Create your models here.


class ExamType(models.Model):

    description = models.CharField(max_length=50)
    name_class = models.CharField(max_length=50)


class Exam(models.Model):
    request_date = models.DateField()
    receipt_date = models.DateField()
    speciment_collection_date = models.DateField()
    received_speciment = models.CharField(max_length=50, null=True, blank=True)
    examination_time = models.TimeField()
    requesting_physician = models.CharField(max_length=50)
    responsible_physician = models.CharField(max_length=50)
    exam_type = models.ForeignKey(ExamType)
    patient = models.BigIntegerField()


class ReportStatus(models.Model):
    description = models.CharField(max_length=50)
