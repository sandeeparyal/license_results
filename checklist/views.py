from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
#from django.core import serializers
from django.http import JsonResponse
#from django.contrib import messages

from datetime import date

from django.contrib.auth.decorators import login_required
from .models import Officer, ExamType, Examination, Checklist, LicenseType
from .forms import ExaminationForm

# Create your views here.


@login_required
def index(request):
    collect_new_files()
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

def collect_new_files():
    import os
    directory_path = "media/checklist/"
    for filename in os.listdir(directory_path):
        filepath = os.path.join('checklist/', filename)
        year, month, day = filename[0:4], filename[5:7], filename[8:10]
        checklist = Checklist.objects.create(checklist_name=filename, checklist_file=filepath)
        checklist.save()
        import pdb; pdb.set_trace()
        primary_key = 1
        examination = Examination.objects.create(passed_candidate=0, failed_candidate=0, absent_candidate=0, traffic_officers = "Non", examination_type=ExamType.objects.get(pk=primary_key), examination_license_type=LicenseType.objects.get(pk=primary_key), examination_officer=Officer.objects.get(pk=primary_key), examination_checklist=checklist)
        examination.save()


'''
class Examination(models.Model):
    examination_date = models.DateField(default=date.today)
    passed_candidate = models.IntegerField(default=0)
    failed_candidate = models.IntegerField(default=0)
    absent_candidate = models.IntegerField(default=0)
    traffic_officers = models.CharField(max_length=200)

    examination_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    examination_license_type = models.ForeignKey(LicenseType, on_delete=models.CASCADE, blank=True)
    examination_officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    examination_checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)

    def candidates(self):
        return(self.passed_candidate+self.failed_candidate+self.absent_candidate)

    def __str__(self):
        return(str(self.examination_date))
'''
