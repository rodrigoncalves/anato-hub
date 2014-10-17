from django.shortcuts import render
from models import Cytology
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here
def new_cytology(request):
	cytology = Cytology()
	return render_to_response(
		'new_cytology.html', {
			"cytology" : cytology
		},
		context_instance = RequestContext(request)
	)

def add_cytology(request):
	clinical_information = request.POST.get('clinical_information')
	quantity = request.POST.get('quantity')
	microscopic = request.POST.get('microscopic')
	conclusion = request.POST.get('conclusion')
	note = request.POST.get('note')
	footer = request.POST.get('footer')

	cytology = Cytology(
		clinical_information = clinical_information,
		quantity = quantity,
		microscopic = microscopic,
		conclusion = conclusion,
		note = note,
		footer = footer
	)

	cytology.save()

	return render_to_response(
		'home_search.html',
		context_instance = RequestContext(request)
	)