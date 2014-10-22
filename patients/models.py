from __future__ import unicode_literals

from django.db import models

class Paciente(models.Model):
    codigo = models.IntegerField(blank=True, primary_key = True) #removido null=True.
    nome = models.CharField(max_length=255, blank=True) #Valor maximo
    cpf = models.CharField(max_length=12, blank=True) ##1 digito a mais de CPF, por garantia.
    nome_mae = models.CharField(max_length=255, blank=True)
    nome_pai = models.CharField(max_length=255, blank=True)
    dt_nascimento = models.DateTimeField(blank=True, null=True)
    nac_codigo = models.IntegerField(blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True)
    sexo = models.CharField(max_length=25, blank=True)
    naturalidade = models.CharField(max_length=100, blank=True)
    prontuario = models.IntegerField(blank=True, null=True)
    dt_obito = models.DateTimeField(blank=True, null=True)
    rg = models.CharField(max_length=12, blank=True)
    observacao = models.CharField(max_length=255, blank=True)
    prnt_ativo = models.CharField(max_length=255, blank=True)
    sexo_biologico = models.CharField(max_length=50, blank=True)
    nro_cartao_saude = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'paciente'

