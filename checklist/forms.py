from django import forms
from django.forms import ModelForm
from .models import Officer, ExamType, LicenseType, Checklist, Examination
import datetime

class ExaminationForm(ModelForm):
    class Meta:
        model = Examination
        fields = ["examination_date", "examination_type", "examination_license_type"]
        widgets = {
            'examination_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }
