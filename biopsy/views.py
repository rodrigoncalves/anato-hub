# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from models import Biopsy

@login_required(login_url='/', redirect_field_name='')
def new_biopsy(request):
    biopsy = Biopsy()
    return render_to_response(
        'new_biopsy.html', { 
            "biopsy" : biopsy
        },
        context_instance=RequestContext(request)
    )

@login_required(login_url='/', redirect_field_name='')
def add_biopsy(request):
	clinical_information = request.POST.get('clinical_information')
	macroscopic = request.POST.get('macroscopic')
	microscopic = request.POST.get('microscopic')
	conclusion = request.POST.get('conclusion')
	note = request.POST.get('note')
	footer = request.POST.get('footer')

	biopsy = Biopsy(
		clinical_information=clinical_information,
		macroscopic=macroscopic,
		microscopic=microscopic,
		conclusion=conclusion,
		note=note,
		footer=footer
	)

	biopsy.save()

	return render_to_response(
	    'home_search.html',
	    context_instance=RequestContext(request)
	)
