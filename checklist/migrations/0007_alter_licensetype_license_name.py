# Generated by Django 4.2.4 on 2023-08-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0006_alter_examtype_exam_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licensetype',
            name='license_name',
            field=models.CharField(choices=[('C1', 'C1'), ('J2', 'J2'), ('J5', 'J5'), ('G', 'G'), ('D', 'D'), ('E', 'E'), ('B', 'B'), ('X', 'Not Applicable'), ('C', 'C'), ('J4', 'J4'), ('J3', 'J3'), ('I1', 'I1'), ('J1', 'J1'), ('F', 'F'), ('I', 'I'), ('I3', 'I3'), ('A', 'A'), ('H', 'H'), ('K', 'K'), ('I2', 'I2')], max_length=20),
        ),
    ]
