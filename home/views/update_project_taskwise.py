from django.shortcuts import render, redirect
from home.models.company import Company
from home.models.employe import Employe
from home.models.project import Project
from home.models.student import Student
from django.core.mail import send_mail
from datetime import date, datetime
from django.views import View
from credma import settings

class UpdateProjectTaskwise(View):
    def get(self, request):
        try: 
            if request.session['employee']:
                return redirect('e_project')
        except:
            return redirect('e_login')
        
    def post(self, request):
        description = request.POST.get('description')
        status = int(request.POST.get('status'))

        description_1 = request.POST.get('description_1')
        duration_1 = request.POST.get('duration_1')
        
        description_2 = request.POST.get('description_2')
        duration_2 = request.POST.get('duration_2')
        
        description_3 = request.POST.get('description_3')
        duration_3 = request.POST.get('duration_3')
        
        description_4 = request.POST.get('description_4')
        duration_4 = request.POST.get('duration_4')
        
        description_5 = request.POST.get('description_5')
        duration_5 = request.POST.get('duration_5')
        
        description_6 = request.POST.get('description_6')
        duration_6 = request.POST.get('duration_6')
        
        description_7 = request.POST.get('description_7')
        duration_7 = request.POST.get('duration_7')
        
        description_8 = request.POST.get('description_8')
        duration_8 = request.POST.get('duration_8')
        
        description_9 = request.POST.get('description_9')
        duration_9 = request.POST.get('duration_9')
        
        description_10 = request.POST.get('description_10')
        duration_10 = request.POST.get('duration_10')
        
        description_11 = request.POST.get('description_11')
        duration_11 = request.POST.get('duration_11')
        
        description_12 = request.POST.get('description_12')
        duration_12 = request.POST.get('duration_12')
        
        pro_id = request.POST.get('pro_id')
        last_update = datetime.today()


        project = Project.objects.get(id=pro_id)
        
        project.Status = status
        project.Last_update = last_update

        if(description):
            project.Description = description

        if(description_1):
            project.Description_1 = description_1
        if(duration_1):
            dur = duration_1.split('-')
            duration_1 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_1>project.Duration_1:
                project.Duration_1 = duration_1
            
        if(description_2):
            project.Description_2 = description_2
        if(duration_2):
            dur = duration_2.split('-')
            duration_2 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_2>project.Duration_2:
                project.Duration_2 = duration_2
            
        if(description_3):
            project.Description_3 = description_3
        if(duration_3):
            dur = duration_3.split('-')
            duration_3 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_3>project.Duration_3:
                project.Duration_3 = duration_3
            
        if(description_4):
            project.Description_4 = description_4
        if(duration_4):
            dur = duration_4.split('-')
            duration_4 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_4>project.Duration_4:
                project.Duration_4 = duration_4
            
        if(description_5):
            project.Description_5 = description_5
        if(duration_5):
            dur = duration_5.split('-')
            duration_5 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_5>project.Duration_5:
                project.Duration_5 = duration_5
            
        if(description_6):
            project.Description_6 = description_6
        if(duration_6):
            dur = duration_6.split('-')
            duration_6 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_6>project.Duration_6:
                project.Duration_6 = duration_6
            
        if(description_7):
            project.Description_7 = description_7
        if(duration_7):
            dur = duration_7.split('-')
            duration_7 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_7>project.Duration_7:
                project.Duration_7 = duration_7
            
        if(description_8):
            project.Description_8 = description_8
        if(duration_8):
            dur = duration_8.split('-')
            duration_8 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_8>project.Duration_8:
                project.Duration_8 = duration_8
            
        if(description_9):
            project.Description_9 = description_9
        if(duration_9):
            dur = duration_9.split('-')
            duration_9 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_9>project.Duration_9:
                project.Duration_9 = duration_9
            
        if(description_10):
            project.Description_10 = description_10
        if(duration_10):
            dur = duration_10.split('-')
            duration_10 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_10>project.Duration_10:
                project.Duration_10 = duration_10
            
        if(description_11):
            project.Description_11 = description_11
        if(duration_11):
            dur = duration_11.split('-')
            duration_11 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_11>project.Duration_11:
                project.Duration_11 = duration_11
            
        if(description_12):
            project.Description_12 = description_12
        if(duration_12):
            dur = duration_12.split('-')
            duration_12 = date(int(dur[0]), int(dur[1]), int(dur[2]))
            if duration_12>project.Duration_12:
                project.Duration_12 = duration_12

        try:
            if(project.Student):
                stu = project.Student
                student = Student.objects.get(Email=stu)
                    
                project.save()

                body = 'Project: '+project.Name + " is Updated. Check the project details again and if updations are not suitable to you than contact to your TPO or CREDEMA."
                subject = "CREDEMA Projects - Project Updation"

                send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                return redirect('e_project')
            
        except:
            return redirect('e_project')