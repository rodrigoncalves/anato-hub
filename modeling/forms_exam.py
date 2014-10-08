# -*- coding: utf-8 -*-

from django import forms

class ExamForm(forms.Form):
    
    request_date = forms.DateField()
    receipt_date = forms.DateField()
    speciment_collection_date = forms.DateField()
    received_speciment = forms.CharField()
    examination_time = forms.TimeField()
    requesting_physician = forms.CharField()
    responsible_physician = forms.CharField()
    FIELDNAME = forms.TimeField()