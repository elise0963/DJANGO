# Generated by Django 4.2.6 on 2023-10-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='est_date',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
