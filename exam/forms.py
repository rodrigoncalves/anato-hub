# -*- coding: utf-8 -*-

from exam.models import Exam
from core.utils import convert_date_format


def get_exam_form(request):
    exam = Exam()
    exam.request_date = convert_date_format(request.POST.get('request_date'))
    exam.receipt_date = convert_date_format(request.POST.get('receipt_date'))
    exam.speciment_collection_date = convert_date_format(request.POST.get(
        'speciment_collection_date'))
    exam.received_speciment = request.POST.get('received_speciment')
    exam.examination_time = request.POST.get('examination_time')
    exam.requesting_physician = request.POST.get('request_date')
    exam.responsible_physician = request.POST.get('responsible_physician')
    exam.exam_type_id = request.POST.get('exam_type_id', 1)

    return exam
