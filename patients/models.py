from __future__ import unicode_literals

from django.db import models

class Paciente(models.Model):
    codigo = models.IntegerField(blank=True, null=True, primary_key = True)
    nome = models.CharField(max_length=-1, blank=True)
    cpf = models.CharField(max_length=-1, blank=True)
    nome_mae = models.CharField(max_length=-1, blank=True)
    nome_pai = models.CharField(max_length=-1, blank=True)
    dt_nascimento = models.DateTimeField(blank=True, null=True)
    nac_codigo = models.IntegerField(blank=True, null=True)
    cor = models.CharField(max_length=-1, blank=True)
    sexo = models.CharField(max_length=-1, blank=True)
    naturalidade = models.CharField(max_length=-1, blank=True)
    prontuario = models.IntegerField(blank=True, null=True)
    dt_obito = models.DateTimeField(blank=True, null=True)
    rg = models.CharField(max_length=-1, blank=True)
    observacao = models.CharField(max_length=-1, blank=True)
    prnt_ativo = models.CharField(max_length=-1, blank=True)
    sexo_biologico = models.CharField(max_length=-1, blank=True)
    nro_cartao_saude = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'paciente'

