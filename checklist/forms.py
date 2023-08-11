from django import forms
from django.forms import ModelForm
from django.contrib import messages
from .models import Officer, ExamType, LicenseType, Checklist, Examination
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class ExaminationForm(ModelForm):
    examination_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Examination
        fields = ["examination_date", "examination_type", "examination_license_type"]
        
