# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from models import Cytology


@login_required(login_url='/', redirect_field_name='')
def register_cytology(request):
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

    return redirect('/exame/%d' % cytology.exam.id)