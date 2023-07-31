from django import forms
from django.forms import ModelForm
from .models import Checklist
import datetime

class ChecklistForm(ModelForm):
    class Meta:
        model = Checklist
        fields = ["checklist_date", "checklist_type", "checklist_category"]
        widgets = {
            'checklist_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }
