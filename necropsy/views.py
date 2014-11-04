# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from necropsy.models import Necropsy


@login_required(login_url='/', redirect_field_name='')
def new_necropsy(request):
    return render_to_response(
        'new_necropsy.html',
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def add_necropsy(request):
    clinical_information = request.POST['clinical_information']
    macroscopic = request.POST['macroscopic']
    microscopic = request.POST['microscopic']
    conclusion = request.POST['conclusion']
    notes = request.POST['notes']
    footer = request.POST['footer']

    necropsy = Necropsy(
        clinical_information=clinical_information,
        macroscopic=macroscopic,
        microscopic=microscopic,
        conclusion=conclusion,
        notes=notes,
        footer=footer
    )

    necropsy.save()

    return render_to_response(
        'home_search.html',
        context_instance=RequestContext(request)
    )
