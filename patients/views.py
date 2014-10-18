from django.shortcuts import render_to_response
from django.template import RequestContext
from patients.models import Paciente

def search_results(request):
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
    patients_temp = Paciente.objects.using('hub').filter(nome__icontains = patient_name) & Paciente.objects.using('hub').filter(prontuario__icontains = report_id) & Paciente.objects.using('hub').filter(dt_nascimento__icontains = birth_date) & Paciente.objects.using('hub').filter(nome_mae__icontains = mother_name)

    #Selecionando somente os 10 primeiros pacientes.    
    patients = patients_temp[0:10]

    return {"patients": patients}


def home_search(request):
    return render_to_response(
        'home_search.html',
        context_instance=RequestContext(request)
    )
