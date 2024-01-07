from django.shortcuts import render,redirect
from home.models.employe import Employe
from home.models.student import Student
from home.models.project import Project
from django.core.mail import send_mail
from datetime import date, timedelta
from django.views import View
from credma import settings

class EmployeProject(View):
    def get(self, request):
        try:
            if request.session['employee']:
                emp = request.session['employee']
                employe = Employe.objects.get(id=emp)
                projects = Project.objects.filter(Employe=employe, Status='False')
                data = {}
                
                pro = Project.objects.filter(Employe=employe).exclude(Student=None)
                for i in pro:
                    stu = i.Student
                    student = Student.objects.get(Email=stu)
                    
                    if student.is_Suspended:
                        pass
                    
                    else:
                        if date.today() == i.Duration-timedelta(days=15):
                            body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                            subject = "CREDEMA - WARNING"
                            res = send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                        
                        elif date.today() == i.Duration-timedelta(days=7):
                            body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                            subject = "CREDEMA - WARNING"
                            res = send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                            
                        elif date.today() == i.Duration-timedelta(days=1):
                            body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                            subject = "CREDEMA - LAST WARNING"
                            res = send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                        
                        elif date.today() == i.Duration:
                            body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                            subject = "CREDEMA - WARNING"
                            res = send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                        
                        elif date.today() > i.Duration:
                            body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                            subject = "CREDEMA - ACCOUNT SUSPENDED"
                            res = send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                            student.is_Suspended = True
                            student.Suspend_till = date.today()+timedelta(days=21)
                            student.save()
                            i.Student = None
                            i.save()
                        else:
                            pass
                                                

                data['projects'] = projects
                data['employe'] = employe

                return render(request, 'e_project.html', data)
        except:
            return redirect('e_login')