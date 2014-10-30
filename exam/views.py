# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from exam.models import ExamType, Exam
from exam.forms import get_exam_form
from exam.dynamic_import import create_specific_exam
from patients.models import Paciente


@login_required()
def new_exam(request):
    exam_types = ExamType.objects.all()
    patient_id = request.POST["patient_id"]
    patient = Paciente.objects.using("hub").get(codigo=patient_id)

    return render_to_response(
        'new_exam.html',
        {"exam_types": exam_types,
         "patient": patient},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def register_exam(request):
    exam = get_exam_form(request)
    exam.save()

    specific_exam = create_specific_exam(
        exam.exam_type.name_class)
    specific_exam.exam = exam
    specific_exam.save()

    exam_types = ExamType.objects.all()
    return render_to_response(
        'new_exam.html',
        {'exam_saved': True, 'exam_types': exam_types},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def visualize_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    exam_type = exam.exam_type.name_class
    exam_type = 'visualize_' + exam_type.lower() + '.html'

    return render_to_response(
        'visualize_exam.html',
        {'exam': exam,
         'patient': exam.patient_information,
         'specific_exam': exam.specific_exam,
         'exam_type': exam_type},
        context_instance=RequestContext(request)
    )
