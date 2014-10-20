from django.shortcuts import render_to_response
from django.template import RequestContext

from exam.models import ExamType
from exam.forms import get_exam_form
from exam.dynamic_import import create_specific_exam

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

    specific_exam = create_specific_exam(
        exam.exam_type.name_class)
    specific_exam.exam = exam
    specific_exam.save()

    exam_types = ExamType.objects.all()
    return render_to_response(
        'new_exam.html',
        {'exam_saved': True, 'exam_types': exam_types},
        context_instance=RequestContext(request)
    )
