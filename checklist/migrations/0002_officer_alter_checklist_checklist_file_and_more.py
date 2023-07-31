# Generated by Django 4.2.3 on 2023-07-28 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checklist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Officer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("officer_name", models.CharField(max_length=200)),
                ("officer_phone", models.CharField(max_length=25)),
                ("officer_designation", models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name="checklist",
            name="checklist_file",
            field=models.FileField(upload_to="checklist/"),
        ),
        migrations.AddField(
            model_name="checklist",
            name="checklist_officer",
            field=models.ManyToManyField(to="checklist.officer"),
        ),
    ]
