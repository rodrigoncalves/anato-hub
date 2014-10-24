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

def import_profile_type():
    from profiletype.models import ProfileType

    with open_csv('profile_type') as csv_file:
        data = csv.reader(csv_file)

        print 'Importing profile type...'
        for row in data:
            profile_type = ProfileType()
            profile_type.id = row[0]
            profile_type.description = row[1]
            profile_type.save()
