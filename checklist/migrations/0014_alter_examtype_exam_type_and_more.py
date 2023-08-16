# Generated by Django 4.2.3 on 2023-08-15 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checklist", "0013_alter_examtype_exam_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="examtype",
            name="exam_type",
            field=models.CharField(
                choices=[("W", "Written"), ("I", "Interview"), ("T", "Trial")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="licensetype",
            name="license_name",
            field=models.CharField(
                choices=[
                    ("I1", "I1"),
                    ("J4", "J4"),
                    ("C", "C"),
                    ("J3", "J3"),
                    ("J2", "J2"),
                    ("B", "B"),
                    ("E", "E"),
                    ("D", "D"),
                    ("C1", "C1"),
                    ("K", "K"),
                    ("I3", "I3"),
                    ("J1", "J1"),
                    ("A", "A"),
                    ("G", "G"),
                    ("I", "I"),
                    ("I2", "I2"),
                    ("H", "H"),
                    ("X", "Not Applicable"),
                    ("J5", "J5"),
                    ("F", "F"),
                ],
                max_length=20,
            ),
        ),
    ]
