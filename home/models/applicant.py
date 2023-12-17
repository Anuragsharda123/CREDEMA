from django.db import models
from .student import Student
from .project import Project



class Applicant(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)