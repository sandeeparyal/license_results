from django.contrib import admin

# Register your models here.

from .models import Checklist, Officer, ExamType, LicenseType, Examination


admin.site.register(Checklist)
admin.site.register(Officer)
admin.site.register(ExamType)
admin.site.register(LicenseType)
admin.site.register(Examination)

