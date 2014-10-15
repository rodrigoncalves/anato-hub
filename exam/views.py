from django.shortcuts import render_to_response
from django.template import RequestContext

from exam.models import ExamType
from exam.forms import get_exam_form

# Create your views here.


def new_exam(request):
    exam_types = ExamType.objects.all()
    return render_to_response(
        'new_exam.html',
        {"exam_types": exam_types},
        context_instance=RequestContext(request)
    )


def register_exam(request):
    exam = get_exam_form(request)
    exam.save()

    exam_type = ExamType.objects.get(id=exam.exam_type_id)

    exam_types = ExamType.objects.all()
    return render_to_response(
        'new_exam.html',
        {'exam_saved': True, 'exam_types': exam_types},
        context_instance=RequestContext(request)
    )
