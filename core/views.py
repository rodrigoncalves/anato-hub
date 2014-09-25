from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.


def home_search(request):
    return render_to_response(
        'home_search.html',
        context_instance=RequestContext(request)
    )


def search_results(request):
    return render_to_response(
        'search_results.html',
        context_instance=RequestContext(request)
    )

def registration_examination(request):
	return render_to_response(
		'registration_examination.html',
		context_instance=RequestContext(request)
	)
