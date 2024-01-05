# Generated by Django 4.2.6 on 2024-01-05 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_student_college_name_student_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='College_name',
        ),
        migrations.AddField(
            model_name='student',
            name='is_Suspended',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='Last_update',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 1, 5, 23, 32, 19, 307995), null=True),
        ),
    ]
