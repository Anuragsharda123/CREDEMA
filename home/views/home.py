from django.shortcuts import render, redirect
from datetime import date, timedelta
from django.core.mail import send_mail
from home.models.student import Student
from home.models.project import Project
from django.views import View
from credma import settings

class Index(View):
    def get(self, request):
        student = None
        # request.session.clear()
        try:
            del request.session['otp']
        except:
            pass
        
        try:
            if request.session['student']:
                stu_id = request.session['student']
                student = Student.objects.get(id=stu_id)
                if student.is_Suspended:
                    return redirect('s_logout')
                else:
                    p = Project.objects.filter(Student=student, Status=False)
                    for i in p:
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
                            return redirect('s_logout')
                        else:
                            pass

        except:
            pass

        search = request.GET.get('search')
        projects = Project.objects.filter(Student=None)
            
        data = {}
        if search:
            search = search.lower()
            projects = Project.get_project_by_search(search)
                    
            
        data['projects'] = projects
        data['student'] = student
        return render(request, "project_list.html", data)
            