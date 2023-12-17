from django.contrib import admin
from .models.company import Company
from .models.student import Student
from .models.employe import Employe
from .models.project import Project
from .models.applicant import Applicant


class AdminCompany(admin.ModelAdmin):
    list_display = ['Name', 'Official_website', 'Official_Email']

class AdminEmploye(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Company_name', 'Role']

class AdminStudent(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Phone']

class AdminProject(admin.ModelAdmin):
    list_display = ['Name', 'Skill_req', 'Perks', 'Duration']

class AdminApplicant(admin.ModelAdmin):
    list_display = ['Project', 'Student']


admin.site.register(Company, AdminCompany)
admin.site.register(Employe, AdminEmploye)
admin.site.register(Project, AdminProject)
admin.site.register(Student, AdminStudent)
admin.site.register(Applicant, AdminApplicant)