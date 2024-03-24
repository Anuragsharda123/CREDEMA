# Generated by Django 4.2.6 on 2024-03-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_project_project_alter_student_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Project',
            field=models.FileField(upload_to='Documents/Projects/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='Documents/Student/Profile_Image/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='Resume',
            field=models.FileField(upload_to='Documents/Student/'),
        ),
    ]
