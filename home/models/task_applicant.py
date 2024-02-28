from django.db import models
from .student import Student
from .project import Project



class Applicant(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Task_1 = models.BooleanField(default=False)
    Task_2 = models.BooleanField(default=False)
    Task_3 = models.BooleanField(default=False)
    Task_4 = models.BooleanField(default=False)
    Task_5 = models.BooleanField(default=False)
    Task_6 = models.BooleanField(default=False)
    Task_7 = models.BooleanField(default=False)
    Task_8 = models.BooleanField(default=False)
    Task_9 = models.BooleanField(default=False)
    Task_10 = models.BooleanField(default=False)
    Task_11 = models.BooleanField(default=False)
    Task_12 = models.BooleanField(default=False)