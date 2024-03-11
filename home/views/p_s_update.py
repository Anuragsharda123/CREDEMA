from django.shortcuts import redirect
from home.models.project import Project
from home.models.employe import Employe
from home.models.student import Student
from django.core.mail import send_mail
from django.views import View
from credma import settings

class P_S_Update(View):
    def get(self, request):
        return redirect('home')
    
    def post(self, request):
        try:
            total = 0
            complete = 0
            stu_id = request.session['student']
            task = int(request.POST.get('task'))
            status = int(request.POST.get('status'))
            pro_id = request.POST.get('pro_id')
            project = Project.objects.get(id=pro_id)
            emp = project.Employe
            employ = Employe.objects.get(Email=emp)
            student = Student.objects.get(id=stu_id)

            if(project.Task_1):
                total = total + 1
                if(project.Status_1):
                    complete = complete + 1
            
            if(project.Task_2):
                total = total + 1
                if(project.Status_2):
                    complete = complete + 1
            
            if(project.Task_3):
                total = total + 1
                if(project.Status_3):
                    complete = complete + 1
            
            if(project.Task_4):
                total = total + 1
                if(project.Status_4):
                    complete = complete + 1
            
            if(project.Task_5):
                total = total + 1
                if(project.Status_5):
                    complete = complete + 1
            
            if(project.Task_6):
                total = total + 1
                if(project.Status_6):
                    complete = complete + 1
            
            if(project.Task_7):
                total = total + 1
                if(project.Status_7):
                    complete = complete + 1
            
            if(project.Task_8):
                total = total + 1
                if(project.Status_8):
                    complete = complete + 1
            
            if(project.Task_9):
                total = total + 1
                if(project.Status_9):
                    complete = complete + 1
            
            if(project.Task_10):
                total = total + 1
                if(project.Status_10):
                    complete = complete + 1
            
            if(project.Task_11):
                total = total + 1
                if(project.Status_11):
                    complete = complete + 1
            
            if(project.Task_12):
                total = total + 1
                if(project.Status_12):
                    complete = complete + 1
            
            if((task==1) and (status==1)):
                project.Status_1 = True
                complete = complete + 1
            if((task==2) and (status==1)):
                project.Status_2 = True
                complete = complete + 1
            if((task==3) and (status==1)):
                project.Status_3 = True
                complete = complete + 1
            if((task==4) and (status==1)):
                project.Status_4 = True
                complete = complete + 1
            if((task==5) and (status==1)):
                project.Status_5 = True
                complete = complete + 1
            if((task==6) and (status==1)):
                project.Status_6 = True
                complete = complete + 1
            if((task==7) and (status==1)):
                project.Status_7 = True
                complete = complete + 1
            if((task==8) and (status==1)):
                project.Status_8 = True
                complete = complete + 1
            if((task==9) and (status==1)):
                project.Status_9 = True
                complete = complete + 1
            if((task==10) and (status==1)):
                project.Status_10 = True
                complete = complete + 1
            if((task==11) and (status==1)):
                project.Status_11 = True
                complete = complete + 1
            if((task==12) and (status==1)):
                project.Status_12 = True
                complete = complete + 1

            progress = round((complete/total)*100)

            if(status==1):
                project.Progress = progress
                project.save()
                    
                body = "Student: "+student.Name.capitalize()+" has completed his/her task. you can now contact to the TPO office or Sudent if you aren't satisfied with student's work or for any other reason."
                subject = "CREDEMA Projects - Task Completion"

                send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])


            return redirect('home')
        except:
            return redirect('home')