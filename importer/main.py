# -*- coding: utf-8 -*-

import csv
import os
from anato import settings


def open_csv(file_name):
    return open(os.path.join(
        settings.BASE_DIR + '/importer/csvs/', file_name + '.csv'), 'r')


def import_exam_type():
    from exam.models import ExamType
    with open_csv('exam_type') as csv_file:
        data = csv.reader(csv_file)

        print 'Importing exam types...'
        for row in data:
            exam_type = ExamType()
            exam_type.id = row[0]
            exam_type.description = row[1]
            exam_type.name_class = row[2]
            exam_type.save()


def import_report_status():
    from exam.models import ReportStatus

    with open_csv('report_status') as csv_file:
        data = csv.reader(csv_file)

        print 'Importing report status...'
        for row in data:
            report_status = ReportStatus()
            report_status.id = row[0]
            report_status.description = row[1]
            report_status.save()


def import_group_permissions():
    from django.contrib.auth.models import Group, Permission

    with open_csv('groups_permissions') as csv_file:
        data = csv.reader(csv_file)

        print 'Importing groups...'
        for row in data:
            group = Group()
            group.id = row[0]
            group.name = row[1]
            group.save()

            for perm in row[2:]:
                permission = Permission.objects.get(name=perm)
                group.permissions.add(permission)


def import_biopsy_status():
    from biopsy.models import BiopsyStatus

    with open_csv('biopsy_status') as csv_file:
        data = csv.reader(csv_file)

        print 'Importing biopsy status...'
        for row in data:
            report_status = BiopsyStatus()
            report_status.id = row[0]
            report_status.description = row[1]
            report_status.save()


def import_necropsy_status():
    from necropsy.models import NecropsyStatus

    with open_csv('necropsy_status') as csv_file:
        data = csv.reader(csv_file)

        print 'Importing necropsy status...'
        for row in data:
            report_status = NecropsyStatus()
            report_status.id = row[0]
            report_status.description = row[1]
            report_status.save()


def import_cytology_status():
    from cytology.models import CytologyStatus

    with open_csv('cytology_status') as csv_file:
        data = csv.reader(csv_file)

        print 'Importing cytology status...'
        for row in data:
            report_status = CytologyStatus()
            report_status.id = row[0]
            report_status.description = row[1]
            report_status.save()


<<<<<<< HEAD
def import_immunohistochemical_status():
    from immunohistochemical.models import ImmunoHistochemicalStatus

    with open_csv('immunohistochemical_status') as csv_file:
        data = csv.reader(csv_file)

        print 'Importing immunohistochemical status...'
        for row in data:
            report_status = ImmunoHistochemicalStatus()
            report_status.id = row[0]
            report_status.description = row[1]
            report_status.save()


def import_freezing_status():
    from freezing.models import FreezingStatus

    with open_csv('freezing_status') as csv_file:
        data = csv.reader(csv_file)

        print 'Importing freezing status...'
        for row in data:
            report_status = FreezingStatus()
            report_status.id = row[0]
            report_status.description = row[1]
            report_status.save()


=======
>>>>>>> 22210c13d7b3c7521c7d15d090a04bac1e38f30f
def import_all():
    import_biopsy_status()
    import_cytology_status()
    import_necropsy_status()
    import_exam_type()
    import_report_status()
    import_group_permissions()
    print 'Done!'
