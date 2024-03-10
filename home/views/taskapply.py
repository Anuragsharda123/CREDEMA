from django.shortcuts import redirect
from home.models.task_applicant import TaskApplicant
from home.models.student import Student
from home.models.project import Project
from home.models.employe import Employe
from django.views import View
from django.core.mail import send_mail
from credma import settings

class TaskApply(View):
    def get(self, request):
        return redirect('home')


    def post(self, request):
        try:
            if request.session['student']:
                
                pro_id = request.POST.get('pro_id')
                stu_id = request.session['student']
                pro = Project.objects.get(id = pro_id)
                stu = Student.objects.get(id=stu_id)

                emp = pro.Employe
                employ = Employe.objects.get(Email=emp)
                
                task_1 = False
                task_2 = False
                task_3 = False
                task_4 = False
                task_5 = False
                task_6 = False
                task_7 = False
                task_8 = False
                task_9 = False
                task_10 = False
                task_11 = False
                task_12 = False


                if(request.POST.get('task_1')):
                    task_1 = True
                if(request.POST.get('task_2')):
                    task_2 = True
                if(request.POST.get('task_3')):
                    task_3 = True
                if(request.POST.get('task_4')):
                    task_4 = True
                if(request.POST.get('task_5')):
                    task_5 = True
                if(request.POST.get('task_6')):
                    task_6 = True
                if(request.POST.get('task_7')):
                    task_7 = True
                if(request.POST.get('task_8')):
                    task_8 = True
                if(request.POST.get('task_9')):
                    task_9 = True
                if(request.POST.get('task_10')):
                    task_10 = True
                if(request.POST.get('task_11')):
                    task_11 = True
                if(request.POST.get('task_12')):
                    task_12 = True
                if(request.POST.get('task_all')):
                    if(pro.Task_1):
                        task_1 = True
                    if(pro.Task_2):
                        task_2 = True
                    if(pro.Task_3):
                        task_3 = True
                    if(pro.Task_4):
                        task_4 = True
                    if(pro.Task_5):
                        task_5 = True
                    if(pro.Task_6):
                        task_6 = True
                    if(pro.Task_7):
                        task_7 = True
                    if(pro.Task_8):
                        task_8 = True
                    if(pro.Task_9):
                        task_9 = True
                    if(pro.Task_10):
                        task_10 = True
                    if(pro.Task_11):
                        task_11 = True
                    if(pro.Task_12):
                        task_12 = True

                try:
                    is_Exist = TaskApplicant.objects.get(Student=stu, Project = pro)
                except:
                    is_Exist = False
                if(not is_Exist):
                    task = TaskApplicant(Student=stu, Project = pro, Task_1 = task_1, Task_2 = task_2,
                                        Task_3 = task_3, Task_4 = task_4, Task_5 = task_5, Task_6 = task_6,
                                        Task_7 = task_7, Task_8 = task_8, Task_9 = task_9, Task_10 = task_10,
                                        Task_11 = task_11, Task_12 = task_12)

                    task.save()

                else:
                    if(pro.Task_1):
                        if(not is_Exist.Task_1):
                            is_Exist.Task_1 = task_1
                
                    if(pro.Task_2):
                        if(not is_Exist.Task_2):
                            is_Exist.Task_2 = task_2
                
                    if(pro.Task_3):
                        if(not is_Exist.Task_3):
                            is_Exist.Task_3 = task_3
                
                    if(pro.Task_4):
                        if(not is_Exist.Task_4):
                            is_Exist.Task_4 = task_4
                
                    if(pro.Task_5):
                        if(not is_Exist.Task_5):
                            is_Exist.Task_5 = task_5
                
                    if(pro.Task_6):
                        if(not is_Exist.Task_6):
                            is_Exist.Task_6= task_6
                
                    if(pro.Task_7):
                        if(not is_Exist.Task_7):
                            is_Exist.Task_7 = task_7
                
                    if(pro.Task_8):
                        if(not is_Exist.Task_8):
                            is_Exist.Task_8 = task_8
                
                    if(pro.Task_9):
                        if(not is_Exist.Task_9):
                            is_Exist.Task_9 = task_9
                
                    if(pro.Task_10):
                        if(not is_Exist.Task_10):
                            is_Exist.Task_10 = task_10
                
                    if(pro.Task_11):
                        if(not is_Exist.Task_11):
                            is_Exist.Task_11 = task_11
                     
                    if(pro.Task_12):
                        if(not is_Exist.Task_12):
                            is_Exist.Task_12 = task_12
                    
                    is_Exist.save()

                if(not request.POST.get('task_all')):
                    if(task_1):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_1+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_2):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_2+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_3):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_3+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_4):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_4+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_5):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_5+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_6):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_6+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_7):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_7+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_8):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_8+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_9):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_9+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_10):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_10+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_11):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_11+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                    if(task_12):
                        body = "Student: "+stu.Name+" have applied for Task: "+ pro.Task_12+" of project: "+pro.Name
                        subject = "CREDEMA Projects - Project Application"

                        send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                else:
                    body = "Student: "+stu.Name+" have applied for all tasks of project: "+pro.Name
                    subject = "CREDEMA Projects - Project Application"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [employ.Email])

                return redirect('home')
        except:
            return redirect('home')