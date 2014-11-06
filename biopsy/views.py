# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from core.decorators import permission_required_with_403
from models import Biopsy
from exam.models import Exam
from patients.models import Paciente


@permission_required_with_403('add_biopsy')
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
    biopsy = Biopsy.objects.get(pk=request.POST['biopsy_id'])
    biopsy.clinical_information = request.POST['clinical_information']
    biopsy.macroscopic = request.POST['macroscopic']
    biopsy.microscopic = request.POST['microscopic']
    biopsy.conclusion = request.POST['conclusion']
    biopsy.note = request.POST['note']
    biopsy.footer = request.POST['footer']

    biopsy.save()

    patient_id = request.POST.get("patient_id")
    patient = Paciente.objects.using("hub").get(codigo=patient_id)

    # exams = Exam.objects.filter(patient=patient_id)

    return redirect('/paciente/' + str(patient.codigo))

    # return render_to_response(
    #     'patient_profile.html',
    #     {"exam_saved": True,
    #      "patient": patient,
    #      "exams": exams},
    #     context_instance=RequestContext(request)
    # )
