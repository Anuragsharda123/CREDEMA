from django.db import models
from .company import Company
from .employe import Employe
from .student import Student as Stu
from django.utils import timezone

class Project(models.Model):
    Name = models.CharField(max_length=100)
    Employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    Project = models.FileField(upload_to='static/Documents/Projects/')
    Perks = models.CharField(max_length=100)
    Skill_req = models.CharField(max_length=100)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Stipend = models.IntegerField(blank=True, null=True, default=5000)
    Student = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None)
    Description = models.CharField(max_length=1000)
    Duration = models.DateField(null=True, blank=True, default=None)
    Status = models.BooleanField(default=False)
    Progress = models.IntegerField(default=0)

    Task_1 = models.CharField(max_length=50, blank=True)
    Description_1 = models.CharField(max_length=50, blank=True)
    Stipend_1 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_1 = models.DateField(null=True, blank=True, default=None)
    Student_1 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_1')
    Status_1 = models.BooleanField(default=False)
    
    Task_2 = models.CharField(max_length=50, blank=True)
    Description_2 = models.CharField(max_length=50, blank=True)
    Stipend_2 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_2 = models.DateField(null=True, blank=True, default=None)
    Student_2 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_2')
    Status_2 = models.BooleanField(default=False)
    
    Task_3 = models.CharField(max_length=50, blank=True)
    Description_3 = models.CharField(max_length=50, blank=True)
    Stipend_3 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_3 = models.DateField(null=True, blank=True, default=None)
    Student_3 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_3')
    Status_3 = models.BooleanField(default=False)
    
    Task_4 = models.CharField(max_length=50, blank=True)
    Description_4 = models.CharField(max_length=50, blank=True)
    Stipend_4 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_4 = models.DateField(null=True, blank=True, default=None)
    Student_4 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_4')
    Status_4 = models.BooleanField(default=False)
    
    Task_5 = models.CharField(max_length=50, blank=True)
    Description_5 = models.CharField(max_length=50, blank=True)
    Stipend_5 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_5 = models.DateField(null=True, blank=True, default=None)
    Student_5 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_5')
    Status_5 = models.BooleanField(default=False)
    
    Task_6 = models.CharField(max_length=50, blank=True)
    Description_6 = models.CharField(max_length=50, blank=True)
    Stipend_6 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_6 = models.DateField(null=True, blank=True, default=None)
    Student_6 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_6')
    Status_6 = models.BooleanField(default=False)
    
    Task_7 = models.CharField(max_length=50, blank=True)
    Description_7 = models.CharField(max_length=50, blank=True)
    Stipend_7 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_7 = models.DateField(null=True, blank=True, default=None)
    Student_7 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_7')
    Status_7 = models.BooleanField(default=False)
    
    Task_8 = models.CharField(max_length=50, blank=True)
    Description_8 = models.CharField(max_length=50, blank=True)
    Stipend_8 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_8 = models.DateField(null=True, blank=True, default=None)
    Student_8 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_8')
    Status_8 = models.BooleanField(default=False)
    
    Task_9 = models.CharField(max_length=50, blank=True)
    Description_9 = models.CharField(max_length=50, blank=True)
    Stipend_9 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_9 = models.DateField(null=True, blank=True, default=None)
    Student_9 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_9')
    Status_9 = models.BooleanField(default=False)
    
    Task_10 = models.CharField(max_length=50, blank=True)
    Description_10 = models.CharField(max_length=50, blank=True)
    Stipend_10 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_10 = models.DateField(null=True, blank=True, default=None)
    Student_10 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_10')
    Status_10 = models.BooleanField(default=False)
    
    Task_11 = models.CharField(max_length=50, blank=True)
    Description_11 = models.CharField(max_length=50, blank=True)
    Stipend_11 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_11 = models.DateField(null=True, blank=True, default=None)
    Student_11 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_11')
    Status_11 = models.BooleanField(default=False)
    
    Task_12 = models.CharField(max_length=50, blank=True)
    Description_12 = models.CharField(max_length=50, blank=True)
    Stipend_12 = models.IntegerField(default=1000, null=True, blank=True)
    Duration_12 = models.DateField(null=True, blank=True, default=None)
    Student_12 = models.ForeignKey(Stu, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='Student_12')
    Status_12 = models.BooleanField(default=False)
    
    Last_update = models.DateField(default=timezone.now)
    
    
    def __str__(self):
        return self.Name
    

    @staticmethod
    def get_project_by_search(search):
        srch = search
        pro = Project.objects.filter(Skill_req__contains = srch, Student=None)
        return pro