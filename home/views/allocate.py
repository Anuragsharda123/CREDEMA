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
            if request.session['student']:
                return redirect('home')
            
        return redirect('e_login')


    def post(self, request):
        pro_id = request.POST.get('pro_id')
        stu_id = request.POST.get('allocate')
        print("stu:  ", stu_id)
        print("pro:  ", pro_id)


        project = Project.objects.get(id=pro_id)
        student = Student.objects.get(id=stu_id)
        project.Student = student
        project.save()

        body = project.Name + ' is allocated to you. Hope you work on it properly and finish it before given deadline.'
        subject = "CREDEMA Projects - Project Allocation"

        send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

        return redirect("e_project")