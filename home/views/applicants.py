from django.shortcuts import render, redirect
from home.models.applicant import Applicant
from home.models.project import Project
from home.models.student import Student
from django.views import View


class Applicants(View):
    def get(self, request):
        pro_id = request.GET.get('pro_id')
        
        project = Project.objects.get(id=pro_id)
        application = Applicant.objects.filter(Project=project).values_list('Student')
        stu_id = []

        for i in application:
            stu_id.append(i[0])

        print("Pro:                    ", project)
        print("App:                    ", application)
        print("Boom:                   ", stu_id)
        return redirect('e_project')



    def post(self, request):
        pass