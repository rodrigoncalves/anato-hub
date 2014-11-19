# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from core.decorators import permission_required_with_403
from models import Biopsy


@login_required(login_url='/', redirect_field_name='')
def register_biopsy(request):
    biopsy = Biopsy.objects.get(pk=request.POST['biopsy_id'])
    biopsy.examination_time = request.POST['examination_time']
    biopsy.clinical_information = request.POST['clinical_information']
    biopsy.macroscopic = request.POST['macroscopic']
    biopsy.microscopic = request.POST['microscopic']
    biopsy.conclusion = request.POST['conclusion']
    biopsy.note = request.POST['note']
    biopsy.footer = request.POST['footer']

    biopsy.save()

    return redirect('/exame/' + str(biopsy.exam.id))
