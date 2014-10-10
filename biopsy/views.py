from django.shortcuts import render
from biopsy.models import Biopsy
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.
def add_biopsy(request):
	
	clinical_information = request.POST.get('clinical_information')
	macroscopic = request.POST.get('macroscopic')
	microscopic = request.POST.get('microscopic')
	conclusion = request.POST.get('conclusion')
	notes = request.POST.get('notes')
	footer = request.POST.get('footer')

	biopsy = Biopsy(
		clinical_information=clinical_information,
		macroscopic=macroscopic,
		microscopic=microscopic,
		conclusion=conclusion,
		notes=notes,
		footer=footer
	)

	biopsy.save()

	return render_to_response(
	    'home_search.html',
	    context_instance=RequestContext(request)
	)

