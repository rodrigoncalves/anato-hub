# -*- coding: utf-8 -*-

from exam.models import Exam, ExamType
from core.utils import convert_date_format


def get_exam_form(request):
    exam = Exam()
    exam.request_date = convert_date_format(
        request.POST['request_date'])
    exam.receipt_date = convert_date_format(
        request.POST['receipt_date'])
    exam.speciment_collection_date = convert_date_format(
        request.POST['speciment_collection_date'])
    exam.received_speciment = request.POST['received_speciment']
    exam.examination_time = request.POST['examination_time']
    exam.requesting_physician = request.POST['requesting_physician']
    exam.responsible_physician = request.POST['responsible_physician']
    exam_type_id = request.POST['exam_type']
    exam.exam_type = ExamType.objects.get(id=exam_type_id)
    exam.patient = request.POST.get('patient_id')

    return exam
