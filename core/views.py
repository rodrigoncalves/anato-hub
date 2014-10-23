# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required(login_url='/', redirect_field_name='')
def home_search(request):
    return render_to_response(
        'home_search.html',
        context_instance=RequestContext(request)
    )
