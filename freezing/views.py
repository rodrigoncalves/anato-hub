# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from core.decorators import permission_required_with_403
from models import Freezing


@permission_required_with_403('add_freezing')
@login_required(login_url='/', redirect_field_name='')
def new_freezing(request):
    freezing = Freezing()
    return render_to_response(
        'new_freezing.html',
        {"freezing": freezing},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def register_freezing(request):
    freezing = Freezing.objects.get(pk=request.POST['freezing_id'])
    freezing.clinical_information = request.POST['clinical_information']
    freezing.macroscopic = request.POST['macroscopic']
    freezing.microscopic = request.POST['microscopic']
    freezing.conclusion = request.POST['conclusion']
    freezing.note = request.POST['note']
    freezing.footer = request.POST['footer']

    freezing.save()

    return redirect('/exame/' + str(freezing.exam.id))
