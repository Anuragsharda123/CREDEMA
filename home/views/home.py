from django.shortcuts import render, redirect
from django.views import View
from home.models.applicant import Applicant
from home.models.student import Student
from home.models.project import Project

class Index(View):
    def get(self, request):
        search = request.GET.get('search')
        projects = Project.objects.all()
        stu = None
        data = {}
        if search:
            search = search.lower()
            projects = Project.get_project_by_search(search)
                
        try:
            stu = request.session['student']
            stud = Student.objects.get(id=stu)
           

        # print(data)
        except:
            pass
        
        data['projects'] = projects
        return render(request, "project_list.html", data)