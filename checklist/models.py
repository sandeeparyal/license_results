from django.db import models
from datetime import date

# Create your models here.


class Officer(models.Model):
    officer_name = models.CharField(max_length=200)
    officer_phone = models.CharField(max_length = 25)
    officer_designation = models.CharField(max_length=200)
    
    def __str__(self):
        return(self.officer_name)


class ExamType(models.Model):
    
    EXAM_WRITTEN = "W"
    EXAM_TRIAL = "T"
    EXAM_INTERVIEW = "I"
    
    EXAM_CHOICES = {
             
        (EXAM_WRITTEN, "Written"),
        (EXAM_TRIAL, "Trial"),
        (EXAM_INTERVIEW, "Interview"),
     }
    
    exam_type = models.CharField(max_length=10, choices=EXAM_CHOICES)
    remarks =  models.CharField(max_length=250)

    def __str__(self):
        return self.get_exam_type_display()
    

class LicenseType(models.Model):

    CATEGORY_A = "A"
    CATEGORY_B = "B"
    CATEGORY_C = "C"
    CATEGORY_C1 = "C1"
    CATEGORY_D = "D"
    CATEGORY_E = "E"
    CATEGORY_F = "F"
    CATEGORY_G = "G"
    CATEGORY_H = "H"
    CATEGORY_I = "I"
    CATEGORY_I1 = "I1"
    CATEGORY_I2 = "I2"
    CATEGORY_I3 = "I3"
    CATEGORY_J1 = "J1"
    CATEGORY_J2 = "J2"
    CATEGORY_J3 = "J3"
    CATEGORY_J4 = "J4"
    CATEGORY_J5 = "J5"
    CATEGORY_K = "K"
    WRITTEN_CATEGORY = "X"

    CATEGORY_CHOICES = {
         (CATEGORY_A, "A"),
         (CATEGORY_B, "B"),
         (CATEGORY_C, "C"),
         (CATEGORY_C1, "C1"),
         (CATEGORY_D, "D"),
         (CATEGORY_E,"E"),
         (CATEGORY_F,"F"),
         (CATEGORY_G, "G"),
         (CATEGORY_H, "H"),
         (CATEGORY_I, "I"),
         (CATEGORY_I1, "I1"),
         (CATEGORY_I2, "I2"),
         (CATEGORY_I3, "I3"),
         (CATEGORY_J1, "J1"),
         (CATEGORY_J2, "J2"),
         (CATEGORY_J3, "J3"),
         (CATEGORY_J4, "J4"),
         (CATEGORY_J5, "J5"),
         (CATEGORY_K, "K"),
         (WRITTEN_CATEGORY, "Not Applicable"),
     }
    
    license_name = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True)
    license_description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return(self.get_license_name_display())

class Checklist(models.Model):
    checklist_name = models.CharField(max_length=20)
    checklist_file = models.FileField(upload_to='checklist/')
    remarks = models.CharField(max_length=200, null=True)

    def __str__(self):
        return(self.checklist_name)


class Examination(models.Model):
    examination_date = models.DateField(default=date.today)
    passed_candidate = models.IntegerField(default=0)
    failed_candidate = models.IntegerField(default=0)
    absent_candidate = models.IntegerField(default=0)
    traffic_officers = models.CharField(max_length=200)
    
    examination_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    examination_license_type = models.ForeignKey(LicenseType, on_delete=models.CASCADE)
    examination_officer = models.ForeignKey(Officer, on_delete=models.CASCADE)
    examination_checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    
    def candidates(self):
        return(self.passed_candidate+self.failed_candidate+self.absent_candidate)

    def __str__(self):
        return(str(self.examination_date))

