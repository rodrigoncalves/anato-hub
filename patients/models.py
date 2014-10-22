from __future__ import unicode_literals

from django.db import models

class Patient(models.Model):
    code = models.IntegerField(blank=True, primary_key = True) #removido null=True.
    name = models.CharField(max_length=255, blank=True) #Valor maximo
    cpf = models.CharField(max_length=12, blank=True) ##1 digito a mais de CPF, por garantia.
    name_mother = models.CharField(max_length=255, blank=True)
    name_father = models.CharField(max_length=255, blank=True)
    dt_birth = models.DateTimeField(blank=True, null=True)
    birth_code = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True)
    sex = models.CharField(max_length=25, blank=True)
    place_birth = models.CharField(max_length=100, blank=True)
    records = models.IntegerField(blank=True, null=True)
    dt_death = models.DateTimeField(blank=True, null=True)
    rg = models.CharField(max_length=12, blank=True)
    observation = models.CharField(max_length=255, blank=True)
    records_active = models.CharField(max_length=255, blank=True)
    biological_sex = models.CharField(max_length=50, blank=True)
    health_card_number = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'paciente'

