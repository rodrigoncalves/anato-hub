from django.template import RequestContext
from django.shortcuts import render_to_response
from exam.models import Exam
from biopsy.models import Biopsy
from patients.models import Paciente

# Create your views here.
def home_search(request):
    return render_to_response(
        'home_search.html',
        context_instance=RequestContext(request)
    )

def search_results(request):
    return render_to_response(
        'search_results.html',
        context_instance=RequestContext(request)
    )

def patient_profile(request, patient_id):
    patient = Paciente.objects.using("hub").get(codigo=patient_id)
    exams = Exam.objects.filter(patient=patient.codigo)
    return render_to_response(
        'patient_profile.html',{
            'patient': patient,
            'exams': exams},
        context_instance=RequestContext(request)
    )
