from django.shortcuts import render, redirect
from home.models.company import Company
from home.models.employe import Employe
from home.models.project import Project
from home.models.student import Student
from django.core.mail import send_mail
from datetime import datetime, date
from django.views import View
from credma import settings


class Updateproject(View):
    def get(self, request):
        try: 
            if request.session['employee']:
                return redirect('e_project')
        except:
            return redirect('e_login')
    

    def post(self, request):

        try:
            if request.session['employee']:
                if request.POST.get('meth')=='get':
                    # try:
                    if request.session['employee']:
                        pro_id = request.POST.get('update')
                        company = Company.objects.all()
                        project = Project.objects.get(id=pro_id)
                        emp_id = request.session['employee']
                        employe = Employe.objects.get(id=emp_id)

                        data = {}

                        data['project'] = project
                        data['company'] = company
                        data['employe'] = employe

                        return render(request, 'updatepro.html', data)
                    # except:
                    #     return redirect('e_login')
                    
                if request.POST.get('meth')=='post':
                    description = request.POST.get('description')
                    duration = request.POST.get('duration')
                    status = int(request.POST.get('status'))
                    pro_id = request.POST.get('pro_id')
                    last_update = datetime.today()
                    
                    project = Project.objects.get(id=pro_id)
    
                    project.Status = status
                    project.Last_update = last_update
                    
                    if description:
                        project.Description = description
                
                    if duration:
                        dur = duration.split('-')
                        duration = date(int(dur[0]), int(dur[1]), int(dur[2]))
                        if duration>project.Duration:
                            project.Duration = duration

                    try:
                        if(project.Student):
                            stu = project.Student
                            student = Student.objects.get(Email=stu)
                    

                        project.save()

                        body = 'Project: '+project.Name + " is Updated. Check the project details again and if updations are suitable aren't to you than contact to your TPO or CREDEMA."
                        subject = "CREDEMA Projects - Project Updation"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                        return redirect('e_project')
                    except:
                        return redirect('emp_profile')
                
        except:
            return redirect('e_login')