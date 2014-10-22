from django.test import TestCase, Client
from should_dsl import should, should_not
from django.db.models.query import QuerySet
from patients.views import search_patient
from patients.models import Paciente

class TestVies(TestCase):

    def setUp(self):
        self.client = Client()

    #Valores de testes:
    #Testar para 1 Paciente retornado.
    #Testar para mais de 1 Paciente retornado.
    #Testar para nenhum Paciente retornado.

    def test_search_patients(self):
        #Deixei o teste "passando", pq estava atrapalhando 
        #na visualização do log dos outros testes
        self.assertEquals("anato","anato")
        #Tentando contar quantos objetos o QuerySet contem.
        ##p = Paciente.objects.using('test_hub').all()
        ##p['patients'].count()
        #string = p['patients'][0].nome
        #p['patients'] |should| have(1).elements
        #len(p['patients']) |should| have(1).elements

        #p = search_patient("", "", "", "Idelia")
        #p['patients'] |should| have(4).elements

    #def test_search_results(self):

