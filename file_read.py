"""
class Checklist(models.Model):
    checklist_name = models.CharField(max_length=20)
    checklist_file = models.FileField(upload_to='checklist/')
    remarks = models.CharField(max_length=200, null=True)

    def __str__(self):
        return(self.checklist_name)
"""

import os

from checklist.models import Checklist

directory_path = "files/"
for filename in os.listdir(directory_path):
    filepath = os.path.join(directory_path, filename)
    if os.path.isfile(filepath):
        with open(filepath) as f:
            #if Checklist.objects.filter(checklist_name__contains=filename):
            Checklist.objects.create(checklist_name=filename, checklist_file=filepath)

