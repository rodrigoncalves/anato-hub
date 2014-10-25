# -*- coding: utf-8 -*-


class DatabaseMock():

    def create_user(self):
        from django.contrib.auth.models import User
        User.objects.create_user('test_user', 'test@email.com', '123456')

    def create_patient(self):
        from patients.models import Paciente
        Paciente.objects.using('hub').create(codigo=1)

    def create_biopsy_status(self):
        from biopsy.models import BiopsyStatus

        BiopsyStatus.objects.create(
            id=1,
            description='Macroscopia')
        BiopsyStatus.objects.create(
            id=2,
            description='Processamento')

    def create_necropsy_status(self):
        from necropsy.models import NecropsyStatus

        NecropsyStatus.objects.create(
            id=1,
            description='Macroscopia')
        NecropsyStatus.objects.create(
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
            description='Necrópsia',
            name_class='Necropsy')
