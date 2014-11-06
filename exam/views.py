# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from exam.models import ExamType, Exam
from exam.forms import get_exam_form, update_exam_form
from core.decorators import permission_required_with_403
from core.dynamic_import import create_specific_exam
from patients.models import Paciente


@permission_required_with_403('exam.add_exam')
@login_required(login_url='/', redirect_field_name='')
def new_exam(request):
    exam_types = ExamType.objects.all()
    patient_id = request.POST["patient_id"]
    patient = Paciente.objects.using("hub").get(codigo=patient_id)

    return render_to_response(
        'new_exam.html',
        {'exam_types': exam_types,
         'patient': patient},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def register_update_exam(request):
    exam = update_exam_form(request)
    exam.save()

    exam_id = request.POST['exam_id']

    return redirect('/exame/visualizar/' + exam_id)


@login_required(login_url='/', redirect_field_name='')
def register_exam(request):
    exam = get_exam_form(request)
    exam.save()

    specific_exam = create_specific_exam(
        exam.exam_type.name_class)
    specific_exam.exam = exam
    specific_exam.save()

    template_exam = 'update_' + exam.exam_type.name_class.lower() + '.html'

    return render_to_response(
        template_exam,
        {'exam': exam,
         'patient': exam.patient_information,
         'specific_exam': specific_exam},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def visualize_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    exam_type = exam.exam_type.name_class
    exam_type = 'visualize_' + exam_type.lower() + '.html'

    return render_to_response(
        'visualize_exam.html',
        {'exam': exam,
         'patient': exam.patient_information,
         'specific_exam': exam.specific_exam,
         'exam_type': exam_type},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def update_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)

    exam_type = exam.exam_type

    exam.request_date = exam.request_date.strftime('%d/%m/%Y')
    exam.receipt_date = exam.receipt_date.strftime('%d/%m/%Y')
    exam.speciment_collection_date = exam.speciment_collection_date.strftime(
        '%d/%m/%Y')
    exam.examination_time = exam.examination_time.strftime('%d/%m/%Y')

    return render_to_response(
        'update_exam.html',
        {'patient': exam.patient_information,
         'exam': exam,
         'exam_type': exam_type},
        context_instance=RequestContext(request)
    )


@login_required(login_url='/', redirect_field_name='')
def update_specific_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    exam_type = exam.exam_type
    specific_exam = exam.specific_exam
    template_exam = 'update_' + exam_type.name_class.lower() + '.html',

    print exam_type.name_class.lower()

    return render_to_response(
        template_exam,
        {'exam': exam,
         'patient': exam.patient_information,
         'exam_type': exam_type,
         exam_type.name_class.lower(): specific_exam},
        context_instance=RequestContext(request)
    )
