from django.db import models
from .company import Company

class Employe(models.Model):
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
    Company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    Role = models.CharField(max_length=200)
    Employee_Id_no = models.BigIntegerField()
    Social1 = models.CharField(max_length=50, blank=True)
    Social2 = models.CharField(max_length=50, blank=True)
    Social3 = models.CharField(max_length=50, blank=True)
    Terms_and_conditions = models.BooleanField(default=True)

    def __str__(self):
        return str(self.Email)