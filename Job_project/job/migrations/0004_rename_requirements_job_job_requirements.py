# Generated by Django 4.2.6 on 2023-10-19 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_rename_title_job_job_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='requirements',
            new_name='job_requirements',
        ),
    ]