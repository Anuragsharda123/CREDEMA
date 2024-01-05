from django.db import models
from .company import Company
from .employe import Employe
from .student import Student
from datetime import datetime

class Project(models.Model):
    Name = models.CharField(max_length=100)
    Employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Project = models.FileField(upload_to='Documents/Projects/')
    Perks = models.CharField(max_length=100)
    Skill_req = models.CharField(max_length=100)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Stipend = models.IntegerField()
    Student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, default=None)
    Description = models.CharField(max_length=1000)
    Duration = models.DateField(null=True)
    Status = models.BooleanField(default=False)
    Last_update = models.DateField(default= datetime.today())
    
    
    def __str__(self):
        return self.Name
    

    @staticmethod
    def get_project_by_search(search):
        srch = search
        pro = Project.objects.filter(Skill_req__contains = srch, Student=None)
        return pro