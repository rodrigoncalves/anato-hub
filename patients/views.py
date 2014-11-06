# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from patients.models import Paciente
from exam.models import Exam


@login_required(login_url='/', redirect_field_name='')
def search_results(request):

    if ('patient' not in request.POST
            and 'report' not in request.POST
            and 'date' not in request.POST
            and 'mother_name' not in request.POST):
        return redirect('/consulta/')

    patient = request.POST['patient']
    report = request.POST['report']
    date = request.POST['date']
    mother = request.POST['mother_name']

    patients = search_patient(patient, report, date, mother)

    return render_to_response(
        'search_results.html',
        patients,
        context_instance=RequestContext(request)
    )


def search_patient(patient_name, report_id, birth_date, mother_name):
    if (patient_name == ""
            and report_id == ""
            and birth_date == ""
            and mother_name == ""):
        empty_fields = True
    else:
        empty_fields = False

    patients_temp = Paciente.objects.using('hub').filter(
        nome__istartswith=patient_name) & Paciente.objects.using('hub').filter(
        prontuario__istartswith=report_id) & Paciente.objects.using('hub').filter(
        nome_mae__istartswith=mother_name)

    # Executes only if a date was infomed by the user
    if birth_date != "":
        birth_date = birth_date[6] + birth_date[7] + birth_date[8] + \
            birth_date[9] + "-" + birth_date[3] + birth_date[4] + \
            "-" + birth_date[0] + birth_date[1]

        patients_temp = patients_temp & Paciente.objects.using('hub').filter(
            dt_nascimento__range=[
                birth_date + " 00:00:00",
                birth_date + " 23:59:59"])

    # Selecting only the first 10 patients
    patients = patients_temp[0:10]

    if patients.count() > 0:
        empty_results = False
    else:
        empty_results = True

    return {"empty_fields": empty_fields,
            "empty_results": empty_results,
            "patients": patients}


@login_required(login_url='/', redirect_field_name='')
def patient_profile(request, patient_id):
    patient = Paciente.objects.using("hub").get(codigo=patient_id)
    exams = Exam.objects.filter(
        patient=patient.codigo).order_by('-request_date')

    return render_to_response(
        'patient_profile.html',
        {'patient': patient,
        'exams': exams},
        context_instance=RequestContext(request)
    )
