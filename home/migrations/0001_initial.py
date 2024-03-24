# Generated by Django 4.2.6 on 2024-03-24 11:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Official_Email', models.EmailField(max_length=254, unique=True)),
                ('Official_website', models.CharField(max_length=1000)),
                ('Registiration_no', models.CharField(max_length=1000)),
                ('Location', models.CharField(max_length=1000)),
                ('Franchise', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Phone', models.BigIntegerField(unique=True)),
                ('Gender', models.CharField(max_length=10)),
                ('Country', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=100)),
                ('Role', models.CharField(max_length=200)),
                ('Employee_Id_no', models.BigIntegerField()),
                ('Social1', models.CharField(blank=True, max_length=50)),
                ('Social2', models.CharField(blank=True, max_length=50)),
                ('Social3', models.CharField(blank=True, max_length=50)),
                ('Terms_and_conditions', models.BooleanField(default=True)),
                ('Company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.company')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Project', models.FileField(upload_to='Documents/Projects/')),
                ('Perks', models.CharField(max_length=100)),
                ('Skill_req', models.CharField(max_length=100)),
                ('Stipend', models.IntegerField(blank=True, default=5000, null=True)),
                ('Description', models.CharField(max_length=1000)),
                ('Duration', models.DateField(blank=True, default=None, null=True)),
                ('Status', models.BooleanField(default=False)),
                ('Progress', models.IntegerField(default=0)),
                ('Task_1', models.CharField(blank=True, max_length=50)),
                ('Description_1', models.CharField(blank=True, max_length=50)),
                ('Stipend_1', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_1', models.DateField(blank=True, default=None, null=True)),
                ('Status_1', models.BooleanField(default=False)),
                ('Task_2', models.CharField(blank=True, max_length=50)),
                ('Description_2', models.CharField(blank=True, max_length=50)),
                ('Stipend_2', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_2', models.DateField(blank=True, default=None, null=True)),
                ('Status_2', models.BooleanField(default=False)),
                ('Task_3', models.CharField(blank=True, max_length=50)),
                ('Description_3', models.CharField(blank=True, max_length=50)),
                ('Stipend_3', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_3', models.DateField(blank=True, default=None, null=True)),
                ('Status_3', models.BooleanField(default=False)),
                ('Task_4', models.CharField(blank=True, max_length=50)),
                ('Description_4', models.CharField(blank=True, max_length=50)),
                ('Stipend_4', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_4', models.DateField(blank=True, default=None, null=True)),
                ('Status_4', models.BooleanField(default=False)),
                ('Task_5', models.CharField(blank=True, max_length=50)),
                ('Description_5', models.CharField(blank=True, max_length=50)),
                ('Stipend_5', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_5', models.DateField(blank=True, default=None, null=True)),
                ('Status_5', models.BooleanField(default=False)),
                ('Task_6', models.CharField(blank=True, max_length=50)),
                ('Description_6', models.CharField(blank=True, max_length=50)),
                ('Stipend_6', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_6', models.DateField(blank=True, default=None, null=True)),
                ('Status_6', models.BooleanField(default=False)),
                ('Task_7', models.CharField(blank=True, max_length=50)),
                ('Description_7', models.CharField(blank=True, max_length=50)),
                ('Stipend_7', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_7', models.DateField(blank=True, default=None, null=True)),
                ('Status_7', models.BooleanField(default=False)),
                ('Task_8', models.CharField(blank=True, max_length=50)),
                ('Description_8', models.CharField(blank=True, max_length=50)),
                ('Stipend_8', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_8', models.DateField(blank=True, default=None, null=True)),
                ('Status_8', models.BooleanField(default=False)),
                ('Task_9', models.CharField(blank=True, max_length=50)),
                ('Description_9', models.CharField(blank=True, max_length=50)),
                ('Stipend_9', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_9', models.DateField(blank=True, default=None, null=True)),
                ('Status_9', models.BooleanField(default=False)),
                ('Task_10', models.CharField(blank=True, max_length=50)),
                ('Description_10', models.CharField(blank=True, max_length=50)),
                ('Stipend_10', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_10', models.DateField(blank=True, default=None, null=True)),
                ('Status_10', models.BooleanField(default=False)),
                ('Task_11', models.CharField(blank=True, max_length=50)),
                ('Description_11', models.CharField(blank=True, max_length=50)),
                ('Stipend_11', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_11', models.DateField(blank=True, default=None, null=True)),
                ('Status_11', models.BooleanField(default=False)),
                ('Task_12', models.CharField(blank=True, max_length=50)),
                ('Description_12', models.CharField(blank=True, max_length=50)),
                ('Stipend_12', models.IntegerField(blank=True, default=1000, null=True)),
                ('Duration_12', models.DateField(blank=True, default=None, null=True)),
                ('Status_12', models.BooleanField(default=False)),
                ('Last_update', models.DateField(default=django.utils.timezone.now)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.company')),
                ('Employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=50)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='Documents/Student/Profile_Image')),
                ('Age', models.IntegerField()),
                ('Phone', models.BigIntegerField(unique=True)),
                ('Gender', models.CharField(max_length=10)),
                ('Country', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=100)),
                ('Passed', models.CharField(max_length=10)),
                ('University_name', models.CharField(max_length=500)),
                ('Course', models.CharField(max_length=200)),
                ('Roll_no', models.BigIntegerField()),
                ('Projects', models.CharField(blank=True, max_length=200)),
                ('Resume', models.FileField(upload_to='Documents/Student/')),
                ('Social1', models.CharField(blank=True, max_length=100)),
                ('Social2', models.CharField(blank=True, max_length=100)),
                ('Social3', models.CharField(blank=True, max_length=100)),
                ('Exp1', models.CharField(blank=True, max_length=50)),
                ('Exp2', models.CharField(blank=True, max_length=50)),
                ('Exp3', models.CharField(blank=True, max_length=50)),
                ('Skills', models.CharField(max_length=1000)),
                ('is_Suspended', models.BooleanField(default=False)),
                ('Suspend_till', models.DateField(default=django.utils.timezone.now)),
                ('Terms_and_conditions', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_1', models.BooleanField(default=False)),
                ('Task_2', models.BooleanField(default=False)),
                ('Task_3', models.BooleanField(default=False)),
                ('Task_4', models.BooleanField(default=False)),
                ('Task_5', models.BooleanField(default=False)),
                ('Task_6', models.BooleanField(default=False)),
                ('Task_7', models.BooleanField(default=False)),
                ('Task_8', models.BooleanField(default=False)),
                ('Task_9', models.BooleanField(default=False)),
                ('Task_10', models.BooleanField(default=False)),
                ('Task_11', models.BooleanField(default=False)),
                ('Task_12', models.BooleanField(default=False)),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.project')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='Student',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_1',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_1', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_10',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_10', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_11',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_11', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_12',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_12', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_2',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_2', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_3',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_3', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_4',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_4', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_5',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_5', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_6',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_6', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_7',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_7', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_8',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_8', to='home.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='Student_9',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Student_9', to='home.student'),
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.project')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
    ]
