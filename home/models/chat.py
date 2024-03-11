from django.db import models
from .employe import Employe
from .project import Project
from .student import Student

class Chat(models.Model):
    Project = models.ForeignKey(Project, on_delete = models.CASCADE)
    Student = models.ForeignKey(Student, on_delete = models.CASCADE)
    Employe = models.ForeignKey(Employe, on_delete = models.CASCADE)
    Message = models.CharField(max_length=3000)