# Generated by Django 4.2.6 on 2023-10-21 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_industry_state_job_job_type_job_industry_job_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='location',
            new_name='city',
        ),
    ]