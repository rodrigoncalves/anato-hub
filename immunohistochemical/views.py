# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from core.decorators import permission_required_with_403
from models import ImmunoHistochemical


@login_required(login_url='/', redirect_field_name='')
def register_immunohistochemical(request):
    immunohistochemical = ImmunoHistochemical.objects.get(pk=request.POST['immunohistochemical_id'])
    immunohistochemical.clinical_information = request.POST['clinical_information']
    immunohistochemical.previous_biopsy = request.POST['previous_biopsy']
    immunohistochemical.conclusion = request.POST['conclusion']
    immunohistochemical.note = request.POST['note']
    immunohistochemical.footer = request.POST['footer']

    immunohistochemical.save()

    return redirect('/exame/' + str(immunohistochemical.exam.id))
