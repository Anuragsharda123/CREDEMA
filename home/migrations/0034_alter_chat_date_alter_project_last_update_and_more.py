# Generated by Django 4.2.6 on 2024-03-13 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_chat_date_chat_task_id_alter_project_last_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 13, 18, 41, 1, 899249, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='Last_update',
            field=models.DateField(default=datetime.datetime(2024, 3, 13, 18, 41, 1, 879260, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='Suspend_till',
            field=models.DateField(default=datetime.datetime(2024, 3, 13, 18, 41, 1, 876263, tzinfo=datetime.timezone.utc)),
        ),
    ]