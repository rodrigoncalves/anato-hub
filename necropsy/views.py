# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from exam.models import Exam
from necropsy.models import Necropsy
from patients.models import Paciente


@login_required(login_url='/', redirect_field_name='')
def new_necropsy(request):
    return render_to_response(
        'new_necropsy.html',
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def register_necropsy(request):
    necropsy = Necropsy.objects.get(pk=request.POST['necropsy_id'])
    necropsy.clinical_information = request.POST['clinical_information']
    necropsy.main_disease = request.POST['main_disease']
    necropsy.consequential_final_disease = request.POST['consequential_final_disease']
    necropsy.contributors_disease = request.POST['contributors_disease']
    necropsy.consequential_disease = request.POST['consequential_disease']
    necropsy.other_diseases = request.POST['other_diseases']
    necropsy.note = request.POST['note']
    necropsy.footer = request.POST['footer']

    necropsy.save()

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
