from django.db import models
from datetime import date

# Create your models here.


class Officer(models.Model):
    officer_name = models.CharField(max_length=200)
    officer_phone = models.CharField(max_length = 25)
    officer_designation = models.CharField(max_length=200)
    
    def __str__(self):
        return(self.officer_name)


class Checklist(models.Model):
    
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
 
    CHECKLIST_EXAM_WRITTEN = "W"
    CHECKLIST_EXAM_TRIAL = "T"
    CHECKLIST_EXAM_INTERVIEW = "I"

    CHECKLIST_CATEGORY_CHOICES = {
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

    CHECKLIST_EXAM_CHOICES = {
             
        (CHECKLIST_EXAM_WRITTEN, "Written"),
        (CHECKLIST_EXAM_TRIAL, "Trial"),
        (CHECKLIST_EXAM_INTERVIEW, "Interview"),
     }

    checklist_name = models.CharField(max_length=20)
    checklist_type = models.CharField(max_length=1, choices=CHECKLIST_EXAM_CHOICES, default=CHECKLIST_EXAM_TRIAL)
    checklist_date = models.DateField(default=date.today)
    checklist_category = models.CharField(max_length=2, choices=CHECKLIST_CATEGORY_CHOICES, default=CATEGORY_A)
    checklist_file = models.FileField(upload_to='checklist/')
    checklist_officer = models.ManyToManyField(Officer)


    def __str__(self):
        return(self.checklist_name)

