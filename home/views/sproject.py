from django.shortcuts import render
from home.models.student import Student
from home.models.project import Project
from datetime import date
from django.views import View

class StudentProject(View):
    def get(self, request):

        # try:
        stu = request.session['student']
        student = Student.objects.get(id=stu)
        projects = Project.objects.filter(Student=student)
        data = {}
        
        
        data['projects'] = projects
        data['student'] = student

        return render(request, 's_project.html', data)
        # except:
            # return redirect('s_login')
