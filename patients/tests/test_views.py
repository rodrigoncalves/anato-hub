# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from patients.views import search_patient
from patients.models import Paciente
from core.tests.db_mock import DatabaseMock
from django.utils import timezone
from sys import stderr
from should_dsl import should, should_not
from core.tests.format_test import FormatTest


class TestViews(FormatTest, TestCase):
    def setUp(self):
        self.my_type = '[Patients - Views]'
        stderr.write(self.__str__())
        self.db_mock = DatabaseMock()
        self.db_mock.create_patient()
        self.db_mock.create_user()
        self.client = Client()
        self.client.login(username='test_user', password='123456')
    
    def test_patient_profile(self):
        patient = Paciente.objects.using('hub').get(codigo = 1)
        response = self.client.get('/paciente/' + str(patient.codigo))
        response.status_code | should | equal_to(200)
        #Verifying if the patient name is on HTML content.
        self.assertContains(response, patient.nome)

    def test_search_results(self):
        patient = Paciente.objects.using('hub').get(codigo = 1)
        response = self.client.get('/resultados/')
        response.status_code | should | equal_to(302)
        response = self.client.post('/resultados/', {'patient':patient.nome, 'report':patient.prontuario, 'date':'', 'mother_name':''})
        response.status_code | should | equal_to(200)      
        self.assertContains(response, patient.nome)


    def test_search_patient(self):
        #Search for 1 Patient.
        patients_result = search_patient('Test Patient', '', '', '')
        patients_result["empty_results"] | should | be(False)    
        patients_result["empty_fields"] | should | be(False)
        patients_result["patients"].count() | should | be(1)
        patients_result["patients"][0].nome | should | equal_to('Test Patient')        

        #Search for more than 1 Patient.
        patient = Paciente()
        patient.codigo = 2
        patient.nome = 'Test Patient2'
        patient.cpf = '11111111111'
        patient.nome_mae = 'Patient Mother'
        patient.nome_pai = 'Patient Father'
        patient.dt_nascimento = timezone.now()
        patient.nac_codigo = 1
        patient.cor = 'Test Color'
        patient.sexo = 'Male'
        patient.naturalidade = 'Test'
        patient.prontuario = 111111111
        patient.dt_obito = timezone.now()
        patient.rg = '111'
        patient.observacao = ''
        patient.prnt_ativo = 'Active'
        patient.sexo_biologico = 'Male'
        patient.nro_cartao_saude = 1111111
        patient.save(using='hub')
        patients_result = search_patient('Test','','','')
        patients_result["empty_results"] | should | be(False)    
        patients_result["empty_fields"] | should | be(False)
        patients_result["patients"].count() | should | be(2)
        patients_result["patients"][0].nome | should | equal_to('Test Patient')
        patients_result["patients"][1].nome | should | equal_to('Test Patient2')          

        #Search for 0 Patient.
        patients_result = search_patient('Nothing','','','')
        patients_result["empty_results"] | should | be(True)    
        patients_result["empty_fields"] | should | be(False)
        patients_result["patients"].count() | should | be(0)

        #Search for empty fields
        patients_result = search_patient('','','','')
        patients_result["empty_fields"] | should | be(True)

        

