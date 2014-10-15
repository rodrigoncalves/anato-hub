from django import forms
from modeling.exam import Exam
from modeling.report import ReportStatus


class BiopsyStatus(forms.Form):
    description = forms.CharField(max_length=50)


class Biopsy(forms.Form):
    clinical_information = forms.CharField()
    macroscopic = forms.CharField()
    microscopic = forms.CharField()
    conclusion = forms.CharField()
    note = forms.CharField()
    footer = forms.CharField()
    #status = forms.ForeignKey(BiopsyStatus)
    #exam = forms.ForeignKey(Exam)


class BiopsyReport(forms.Form):
    clinical_information = forms.CharField()
    macroscopic = forms.CharField()
    microscopic = forms.CharField()
    conclusion = forms.CharField()
    note = forms.CharField()
   # status = forms.ForeignKey(ReportStatus)
    #biopsy = forms.ForeignKey(Biopsy)
