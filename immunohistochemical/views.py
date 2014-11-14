# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from models import ImmunoHistochemical


@login_required(login_url='/', redirect_field_name='')
def register_immunohistochemical(request):
    clinical_information = request.POST.get('clinical_information')
    previous_biopsy = request.POST.get('previous_biopsy')
    conclusion = request.POST.get('conclusion')
    note = request.POST.get('note')
    footer = request.POST.get('footer')

    immunohistochemical = ImmunoHistochemical(
        clinical_information=clinical_information,
        previous_biopsy=previous_biopsy,
        conclusion=conclusion,
        note=note,
        footer=footer
    )

    immunohistochemical.save()

    return redirect('/exame/%d' % immunohistochemical.exam.id)
