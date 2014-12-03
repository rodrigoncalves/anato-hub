# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from core.decorators import permission_required_with_403
from models import Cytology


@login_required(login_url='/', redirect_field_name='')
def register_cytology(request):
    cytology = Cytology.objects.get(pk=request.POST['cytology_id'])
    cytology.examination_time = request.POST['examination_time']
    cytology.clinical_information = request.POST['clinical_information']
    cytology.quantity = request.POST['quantity']
    cytology.microscopic = request.POST['microscopic']
    cytology.conclusion = request.POST['conclusion']
    cytology.note = request.POST['note']
    cytology.footer = request.POST['footer']

    cytology.save()

    return redirect('/exame/' + str(cytology.exam.id))
