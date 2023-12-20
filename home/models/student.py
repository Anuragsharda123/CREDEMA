from django.db import models

class Student(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=100)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Phone = models.BigIntegerField(unique=True)
    Gender = models.CharField(max_length=10)
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    Passed = models.CharField(max_length=10)
    University_name = models.CharField(max_length=500)
    Course = models.CharField(max_length=200)
    Roll_no = models.BigIntegerField()
    Resume = models.FileField(upload_to='Documents/Student/')
    Social1 = models.CharField(max_length=50, blank=True)
    Social2 = models.CharField(max_length=50, blank=True)
    Social3 = models.CharField(max_length=50, blank=True)
    Skills = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.Email)