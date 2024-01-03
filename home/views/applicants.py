from django.shortcuts import render, redirect
from home.models.applicant import Applicant
from home.models.project import Project
from home.models.employe import Employe
from home.models.student import Student
from django.views import View


class Applicants(View):
    def get(self, request):
        try:
            if request.session['employee']:
                return redirect('e_project')
        except:
            if request.session['student']:
                return redirect('home')
            
        return redirect('e_login')


    def post(self, request):
        pro_id = request.POST.get('pro_id')

        project = Project.objects.get(id=pro_id)
        application = Applicant.objects.filter(Project=project).values_list('Student')
        emp_id = request.session['employee']
        employe = Employe.objects.get(id=emp_id)
        students = []
        data = {}

        for i in application:
            stu_id = i[0]
            students.append(Student.objects.get(id=stu_id))


        data['students'] = students
        data['project'] = project
        data['employe'] = employe

        return render(request, 'p_applicant.html', data)