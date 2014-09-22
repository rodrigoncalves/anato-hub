# from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.


def sign_in(request):
    return render_to_response('sign_in.html')
