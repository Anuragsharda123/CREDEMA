from django.shortcuts import render,redirect
from home.models.student import Student
from home.models.project import Project
from django.views import View

class StudentProject(View):
    def get(self, request):

        try:
            stu = request.session['student']
            student = Student.objects.get(id=stu)
            projects = Project.objects.filter(Student=student)|Project.objects.filter(Student_1=student)|Project.objects.filter(Student_2=student)|Project.objects.filter(Student_3=student)|Project.objects.filter(Student_4=student)|Project.objects.filter(Student_5=student)|Project.objects.filter(Student_6=student)|Project.objects.filter(Student_7=student)|Project.objects.filter(Student_8=student)|Project.objects.filter(Student_9=student)|Project.objects.filter(Student_10=student)|Project.objects.filter(Student_11=student)|Project.objects.filter(Student_12=student)
            data = {}
            
            data['projects'] = projects
            data['student'] = student

            return render(request, 's_project.html', data)
        except:
            return redirect('s_login')
