# -*- coding: utf-8 -*-

from exam.models import Exam


def get_exam_form(request):
    exam = Exam()
    exam.request_date = request.POST['request_date']
    exam.receipt_date = request.POST['receipt_date']
    exam.speciment_collection_date = request.POST['speciment_collection_date']
    exam.received_speciment = request.POST['received_speciment']
    exam.examination_time = request.POST['examination_time']
    exam.requesting_physician = request.POST['requesting_physician']
    exam.responsible_physician = request.POST['responsible_physician']
    exam.exam_type_id = request.POST['exam_type']

    return exam
