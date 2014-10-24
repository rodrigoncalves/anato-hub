# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from models import Biopsy


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
def add_biopsy(request):
    clinical_information = request.POST['clinical_information']
    macroscopic = request.POST['macroscopic']
    microscopic = request.POST['microscopic']
    conclusion = request.POST['conclusion']
    note = request.POST['note']
    footer = request.POST['footer']

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
