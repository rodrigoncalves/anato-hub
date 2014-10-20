from django.shortcuts import render
from immunohistochemical import Immunohistochemical
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.context import RequestContext
# Create your views here.

def new_immunohistochemical(request):
    immunohistochemical = Immunohistochemical()
    return render_to_response(
        'new_immunohistochemical.html', { 
            "immunohistochemical" : immunohistochemical
        },
        context_instance=RequestContext(request)
    )

def add_immunohistochemical(request):
	
	clinical_information = request.POST.get('clinical_information')
	previous_biopsy = request.POST.get('previous_biopsy')
	conclusion = request.POST.get('conclusion')
	note = request.POST.get('note')
	footer = request.POST.get('footer')

	immunohistochemical = Immunohistochemical(
		clinical_information=clinical_information,
		previous_biopsy=previous_biopsy,
		conclusion=conclusion,
		note=note,
		footer=footer
	)

	immunohistochemical.save()

	return render_to_response(
	    'home_search.html',
	    context_instance=RequestContext(request)
	)
