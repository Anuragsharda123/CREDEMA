from home.models.project import Project
from home.models.student import Student
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views import View
from credma import settings


class Allocate(View):
    def get(self, request):
        try:
            if request.session['employee']:
                return redirect('e_project')
        except:
            try:
                if request.session['student']:
                    return redirect('home')
            except:
                return redirect('e_login')


    def post(self, request):
        pro_id = request.POST.get('pro_id')
        stu_id = request.POST.get('allocate')

        project = Project.objects.get(id=pro_id)
        if project.Student:
            return redirect('e_project')
        
        student = Student.objects.get(id=stu_id)
        
        project.Student = student
        project.save()

        body = 'Project: '+project.Name + ' is allocated to you. Hope you work on it properly and finish it before given deadline.'
        subject = "CREDEMA Projects - Project Allocation"

        send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

        return redirect("e_project")