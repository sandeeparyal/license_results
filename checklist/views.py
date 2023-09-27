from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import Officer, ExamType, Examination, Checklist, LicenseType
from .forms import ExaminationForm

# Create your views here.


@login_required
def index(request):
    if request.method == 'POST':
        form = ExaminationForm(request.POST)
        
        if form.is_valid():
            examination_date = form.cleaned_data['examination_date']
            examination_type = form.cleaned_data['examination_type']
            examination_license_type = form.cleaned_data['examination_license_type']
            checklists = Checklist.objects.filter(examination__examination_date=str(examination_date), examination__examination_type=examination_type, examination__examination_license_type=examination_license_type)
            
            if len(checklists) == 0:
                errors = "No checklists available for the selection"
                return HttpResponseNotFound(errors)
        #        return JsonResponse({'success':False, 'errors': errors})
            else:
                #messages.success(request, "File found")
                checklist_files = []
                for checklist in checklists:
                    checklist_files.append('/media/'+str(checklist.checklist_file))

                return HttpResponse(checklist_files)
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    else: 
        form = ExaminationForm()
        return render(request, 'checklist/index.html', {"form":form }) 








