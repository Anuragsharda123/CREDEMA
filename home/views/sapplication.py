from django.shortcuts import render, redirect
from home.models.applicant import Applicant
from home.models.student import Student
from home.models.project import Project
from django.views import View

class StudentApplication(View):
    def get(self, request):

        # try:
        stu = request.session['student']
        student = Student.objects.get(id=stu)
        pro_index = []
        projects = []
        data = {}

        for i in range(0,len(Applicant.objects.filter(Student=student))):
            pro = Applicant.objects.filter(Student=student).values_list()[i][2]
            pro_index.append(pro)

        for i in pro_index:
            proj = Project.objects.get(id=i)
            projects.append(proj)
            
            
        data['projects'] = projects

        return render(request, 's_application.html',data)
        
        # except:
        #     return redirect('s_login')

