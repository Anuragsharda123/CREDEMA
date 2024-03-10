from django.shortcuts import render, redirect
from home.models.task_applicant import TaskApplicant
from home.models.student import Student
from home.models.project import Project
from django.views import View

class AddTaskApplicant(View):
    def get(self, request):
        return redirect('home')


    def post(self, request):
        try:
            if request.session['student']:
                stu_id = request.session['student']
                pro_id = request.POST.get('pro_id')
                pro = Project.objects.get(id = pro_id)
                stu = Student.objects.get(id=stu_id)
                task = TaskApplicant.objects.get(Student=stu, Project=pro)
                
                data = {}
                data['project'] = pro
                data['student'] = stu
                data['task'] = task

                return render(request, 'task_application.html', data)
        except:
            return redirect('home')