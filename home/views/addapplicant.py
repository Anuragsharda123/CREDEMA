from django.shortcuts import redirect
from home.models.applicant import Applicant
from home.models.student import Student
from home.models.project import Project
from django.views import View
from django.core.mail import EmailMessage, send_mail
from credma import settings

class AddApplicant(View):
    def get(self, request):
        return redirect('home')


    def post(self, request):

        proj = request.POST.get('apply')
        stu = request.session['student']
        project = Project.objects.get(id=proj)
        student = Student.objects.get(id=stu)

        try:
            isExist = Applicant.objects.get(Student=student, Project=project)

            if isExist:  
                return redirect('s_application')
        except:
            apply = Applicant(Student=student, Project=project)

            apply.save()

        body = 'You have applied to Project: ' + project.Name
        subject = "Project Application"

        res = send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

        return redirect('home')