from django.shortcuts import render_to_response
from django.template import RequestContext

def search_results(request):
    #patient = request.POST['patient']
    #report = request.POST['report']
    #date = request.POST['date']
    #mother = request.POST['mother_name']

    #dictionary_params = {}

    #criar metodo para fazer busca no banco de dados

    return render_to_response(
        'search_results.html',
        #{'patient': patient, 'report': report, 'date': date, 'mother': mother},
        context_instance=RequestContext(request)
    )

def home_search(request):
    return render_to_response(
        'home_search.html',
        context_instance=RequestContext(request)
    )
