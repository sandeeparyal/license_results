from django.contrib import admin

# Register your models here.

from .models import Checklist, Officer


admin.site.register(Checklist)
admin.site.register(Officer)
