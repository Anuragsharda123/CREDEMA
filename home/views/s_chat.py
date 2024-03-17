from django.shortcuts import render, redirect
from home.models.project import Project
from home.models.employe import Employe
from home.models.company import Company
from home.models.student import Student
from home.models.chat import Chat
from django.views import View

class S_Chat(View):
    def get(self, request):
        return redirect("home")
    
    def post(self, request):
        task = request.POST.get('task_id')
        student_mail = request.POST.get('student_mail')
        employe_mail = request.POST.get('employee_mail')
        pro_id = request.POST.get('pro_id')

        print(task)
        print(student_mail)
        print(employe_mail)
        print(pro_id)
        return redirect("e_project")
        # return render(request, "chat.html")