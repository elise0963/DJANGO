# Generated by Django 4.2.6 on 2023-10-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_applyjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.PositiveIntegerField(default=35000),
        ),
    ]
