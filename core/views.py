from django.template import RequestContext
from django.shortcuts import render_to_response
from modeling.forms_exam import ExamForm
from biopsy.biopsy import Biopsy

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

def patient_profile(request, records):
    return render_to_response(
        'patient_profile.html',
        context_instance=RequestContext(request)
    )
