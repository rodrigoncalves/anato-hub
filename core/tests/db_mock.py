# -*- coding: utf-8 -*-

from django.utils import timezone


class DatabaseMock():
    def create_user(self):
        from django.contrib.auth.models import User
        user = User.objects.create_user(
            'test_user', 'test@email.com', '123456')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


    def create_patient(self):
        from patients.models import Paciente

        patient = Paciente()
        patient.codigo = 1
        patient.nome = 'Test Patient'
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


    def create_biopsy(self, exam_id):
        from biopsy.models import Biopsy
        biopsy = Biopsy()
        biopsy.clinical_information = 'Clinical Information'
        biopsy.macroscopic = 'Macroscopic'
        biopsy.microscopic = 'Microscopic'
        biopsy.conclusion = 'Conclusion'
        biopsy.note = 'Note'
        biopsy.footer = 'Footer'
        biopsy.exam_id = exam_id
        biopsy.save()

    def create_exam_biopsy(self, patient_id=1):
        from exam.models import Exam

        exam = Exam()
        exam.id = 1
        exam.request_date = timezone.now()
        exam.receipt_date = timezone.now()
        exam.speciment_collection_date = timezone.now()
        exam.received_speciment = 'Speciment'
        exam.requesting_physician = 'Request Physician'
        exam.responsible_physician = 'Responsible Physician'
        exam.exam_type_id = 1
        exam.patient = patient_id
        exam.save()
        self.create_biopsy(exam.id)

    def create_biopsy_status(self):
        from biopsy.models import BiopsyStatus

        BiopsyStatus.objects.create(
            id=1,
            description='Macroscopia')
        BiopsyStatus.objects.create(
            id=2,
            description='Processamento')


    def create_freezing(self, exam_id):
        from freezing.models import Freezing

        freezing = Freezing()
        freezing.clinical_information = 'Clinical Information'
        freezing.macroscopic = 'Macroscopic'
        freezing.microscopic = 'Microscopic'
        freezing.conclusion = 'Conclusion'
        freezing.note = 'Note'
        freezing.footer = 'Footer'
        freezing.exam_id = exam_id
        freezing.save()

    def create_exam_freezing(self):
        from exam.models import Exam

        exam = Exam()
        exam.id = 1
        exam.request_date = timezone.now()
        exam.receipt_date = timezone.now()
        exam.speciment_collection_date = timezone.now()
        exam.received_speciment = 'Speciment'
        exam.examination_time = '00:00:00'
        exam.requesting_physician = 'Request Physician'
        exam.responsible_physician = 'Responsible Physician'
        exam.exam_type_id = 1
        exam.patient = 1
        exam.save()

    def create_freezing_status(self):
        from freezing.models import FreezingStatus

        FreezingStatus.objects.create(
            id=1,
            description='Macroscopia')
        FreezingStatus.objects.create(
            id=2,
            description='Processamento')


    def create_necropsy(self, exam_id):
        from necropsy.models import Necropsy

        necropsy = Necropsy()
        necropsy.clinical_information = 'Clinical Information'
        necropsy.main_disease = 'Main Disease'
        necropsy.consequential_final_disease = 'Consequential Final Disease'
        necropsy.contributors_disease = 'Contributors Disease'
        necropsy.consequential_disease = 'Consequential Disease'
        necropsy.other_diseases = 'Other Diseases'
        necropsy.note = 'Note'
        necropsy.footer = 'Footer'
        necropsy.exam_id = exam_id
        necropsy.save()

    def create_exam_necropsy(self):
        from exam.models import Exam

        exam = Exam()
        exam.id = 1
        exam.request_date = timezone.now()
        exam.receipt_date = timezone.now()
        exam.speciment_collection_date = timezone.now()
        exam.received_speciment = 'Speciment'
        exam.examination_time = '00:00:00'
        exam.requesting_physician = 'Request Physician'
        exam.responsible_physician = 'Responsible Physician'
        exam.exam_type_id = 2
        exam.patient = 1
        exam.save()

    def create_necropsy_status(self):
        from necropsy.models import NecropsyStatus

        NecropsyStatus.objects.create(
            id=1,
            description='Macroscopia')
        NecropsyStatus.objects.create(
            id=2,
            description='Processamento')


    def create_immunohistochemical_status(self):
        from immunohistochemical.models import ImmunoHistochemicalStatus

        ImmunoHistochemicalStatus.objects.create(
            id=1,
            description='Macroscopia')
        ImmunoHistochemicalStatus.objects.create(
            id=2,
            description='Processamento')


    def create_cytology_status(self):
        from cytology.models import CytologyStatus

        CytologyStatus.objects.create(
            id=1,
            description='Macroscopia')
        CytologyStatus.objects.create(
            id=2,
            description='Processamento')


    def create_exam_type(self):
        from exam.models import ExamType

        ExamType.objects.create(
            id=1,
            description='Biópsia',
            name_class='Biopsy')
        ExamType.objects.create(
            id=2,
            description='Autópsia',
            name_class='Necropsy')
        ExamType.objects.create(
            id=3,
            description='Imuno-Histoquímica',
            name_class='ImmunoHistochemical')
        ExamType.objects.create(
            id=4,
            description='Citologia',
            name_class='Cytology')

    def delete_exams(self, patient_id):
        from exam.models import Exam
        from core.dynamic_import import import_class

        exams = Exam.objects.filter(patient=patient_id)
        for exam in exams:
            specific_exam = import_class(exam.exam_type)
            specific_exam.objects.filter(exam_id=exam.id).delete()
        exams.delete()
