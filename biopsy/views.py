# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from models import Biopsy
from exam.models import Exam
from patients.models import Paciente


@login_required(login_url='/', redirect_field_name='')
def new_biopsy(request):
    biopsy = Biopsy()
    return render_to_response(
        'new_biopsy.html', {
            "biopsy": biopsy
        },
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def register_biopsy(request):
    clinical_information = request.POST['clinical_information']
    macroscopic = request.POST['macroscopic']
    microscopic = request.POST['microscopic']
    conclusion = request.POST['conclusion']
    note = request.POST['note']
    footer = request.POST['footer']
    exam_id = request.POST['exam_id']

    biopsy = Biopsy(
        clinical_information=clinical_information,
        macroscopic=macroscopic,
        microscopic=microscopic,
        conclusion=conclusion,
        note=note,
        footer=footer,
        exam_id=exam_id
    )

    biopsy.save()

    patient_id = request.POST.get("patient_id")
    patient = Paciente.objects.using("hub").get(codigo=patient_id)

    exams = Exam.objects.filter(patient=patient_id)

    return render_to_response(
        'patient_profile.html',
        {"exam_saved": True,
        "patient": patient,
        "exams": exams},
        context_instance=RequestContext(request)
    )
