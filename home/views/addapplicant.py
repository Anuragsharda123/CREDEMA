from django.shortcuts import redirect
from home.models.applicant import Applicant
from home.models.student import Student
from home.models.employe import Employe
from home.models.project import Project
from django.views import View
from django.core.mail import send_mail
from credma import settings

class AddApplicant(View):
    def get(self, request):
        return redirect('home')


    def post(self, request):

        try:
            if request.session['student']:
                proj = request.POST.get('apply')
                stu = request.session['student']
                project = Project.objects.get(id=proj)
                emp = project.Employe
                print("booooo:     ", emp)
                employ = Employe.objects.get(Email=emp)
                student = Student.objects.get(id=stu)

                try:
                    isExist = Applicant.objects.get(Student=student, Project=project)

                    if isExist:  
                        return redirect('s_application')
                except:
                    apply = Applicant(Student=student, Project=project)

                    apply.save()

                body = student.Name + ' have applied to Project: ' + project.Name
                subject = "Project Application"

                send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                return redirect('home')
        except:
            return redirect('home')