from django.contrib import admin
from .models.company import Company
from .models.student import Student
from .models.employe import Employe
from .models.project import Project
from .models.applicant import Applicant
from .models.task_applicant import TaskApplicant


class AdminCompany(admin.ModelAdmin):
    list_display = ['Name', 'Official_website', 'Official_Email']

class AdminEmploye(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Company_name', 'Role']

class AdminStudent(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Phone']

class AdminProject(admin.ModelAdmin):
    list_display = ['Name', 'Skill_req', 'Perks', 'Duration', 'Last_update']

class AdminApplicant(admin.ModelAdmin):
    list_display = ['Project', 'Student']

class AdminTaskApplicant(admin.ModelAdmin):
    list_display = ['Project', 'Student', 'Task_1', 'Task_2', 'Task_3', 'Task_4', 'Task_5', 'Task_6', 'Task_7', 'Task_8', 'Task_9', 'Task_10', 'Task_11', 'Task_12', ]


admin.site.register(Company, AdminCompany)
admin.site.register(Employe, AdminEmploye)
admin.site.register(Project, AdminProject)
admin.site.register(Student, AdminStudent)
admin.site.register(Applicant, AdminApplicant)
admin.site.register(TaskApplicant, AdminTaskApplicant)