# Generated by Django 4.2.6 on 2023-10-19 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_rename_requirements_job_job_requirements'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_requirements',
            new_name='requirements',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_title',
            new_name='title',
        ),
    ]