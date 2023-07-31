from django.shortcuts import render
from django.http import FileResponse

from django.contrib.auth.decorators import login_required
from .models import Checklist
from .forms import ChecklistForm

# Create your views here.


@login_required
def index(request):
    if request.method == 'POST':
        form = ChecklistForm(request.POST)
#        import pdb; pdb.set_trace()
        if form.is_valid():
            date = form.cleaned_data['checklist_date']
            checklist_type = form.cleaned_data['checklist_type']
            checklist_category = form.cleaned_data['checklist_category']
            checklists = Checklist.objects.filter(checklist_date=str(date), checklist_type=checklist_type, checklist_category=checklist_category)
            return render(request, 'checklist/preview.html', {"checklists": checklists })
    else: 
        form = ChecklistForm()
        return render(request, 'checklist/index.html', {"form":form }) 



"""
@login_required
def render_file(request):
    date = request.POST['checklist_date']
    checklist_type = request.POST['checklist_type']
    checklist_category = request.POST['checklist_category']
    checklist_file_query = "checklist/"+date+checklist_type+checklist_category+".pdf"
    checklists = Checklist.objects.filter(checklist_file=checklist_file_query)
#    import pdb; pdb.set_trace()
#    for test_file in checklists:
#        return FileResponse(test_file, as_attachment="True", content_type='application/pdf')

    return render(request, 'checklist/preview.html', {"checklists": checklists })
"""





