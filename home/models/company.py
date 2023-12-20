from django.db import models

class Company(models.Model):
    Name = models.CharField(max_length=100)
    Official_Email = models.EmailField(unique=True)
    Official_website = models.CharField(max_length=1000)
    Registiration_no = models.CharField(max_length=1000)
    Location = models.CharField(max_length=1000)
    Franchise = models.IntegerField()

    def __str__(self):
        return self.Official_Email