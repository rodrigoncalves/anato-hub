# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from exam.models import ExamType
from exam.forms import get_exam_form
from exam.dynamic_import import create_specific_exam
from patients.models import Paciente
from core.views import user_belongs_to_groups


@login_required(login_url='/', redirect_field_name='')
def new_exam(request):
    exam_types = ExamType.objects.all()
    patient_id = request.POST.get("patient_id")
    patient = Paciente.objects.using("hub").get(codigo=patient_id)

    if user_belongs_to_groups(request.user, ['Staff Doctor', 'Administrative', 'Assistant Medical', 'Resident Doctor']):
        return render_to_response(
           'new_exam.html',
            {"exam_types": exam_types,
            "patient": patient},
            context_instance=RequestContext(request)
        )

    return render_to_response(
       '403.html',
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

    patient_id = request.POST.get("patient_id")
    exam_type_id = request.POST['exam_type']

    exam_type = ExamType.objects.get(pk=exam_type_id).name_class
    template_exam = 'new_' + exam_type.lower() + '.html'

    return render_to_response(
        template_exam, {
        "exam_id": exam.id,
        "patient_id": patient_id},
        context_instance=RequestContext(request)
    )

