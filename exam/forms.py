# -*- coding: utf-8 -*-

from exam.models import Exam, ExamType
from core.utils import convert_date_format


def get_exam_form(request):
    exam = Exam()
    exam.request_date = convert_date_format(request.POST.get('request_date'))
    exam.receipt_date = convert_date_format(request.POST.get('receipt_date'))
    exam.speciment_collection_date = convert_date_format(request.POST.get(
        'speciment_collection_date'))
    exam.received_speciment = request.POST.get('received_speciment')
    exam.examination_time = request.POST.get('examination_time')
    exam.requesting_physician = request.POST.get('requesting_physician')
    exam.responsible_physician = request.POST.get('responsible_physician')
    exam_type_id = request.POST.get('exam_type')
    exam.exam_type = ExamType.objects.get(id=exam_type_id)
    exam.patient = request.POST["patient_id"]

    return exam
