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

        task_1 = None
        task_2 = None
        task_3 = None
        task_4 = None
        task_5 = None
        task_6 = None
        task_7 = None
        task_8 = None
        task_9 = None
        task_10 = None
        task_11 = None
        task_12 = None

        if(request.POST.get('task_1')):
            task_1 = request.POST.get('task_1')

        if(request.POST.get('task_2')):
            task_2 = request.POST.get('task_2')

        if(request.POST.get('task_3')):
            task_3 = request.POST.get('task_3')

        if(request.POST.get('task_4')):
            task_4 = request.POST.get('task_4')

        if(request.POST.get('task_5')):
            task_5 = request.POST.get('task_5')

        if(request.POST.get('task_6')):
            task_6 = request.POST.get('task_6')

        if(request.POST.get('task_7')):
            task_7 = request.POST.get('task_7')

        if(request.POST.get('task_8')):
            task_8 = request.POST.get('task_8')

        if(request.POST.get('task_9')):
            task_9 = request.POST.get('task_9')

        if(request.POST.get('task_10')):
            task_10 = request.POST.get('task_10')

        if(request.POST.get('task_11')):
            task_11 = request.POST.get('task_11')

        if(request.POST.get('task_12')):
            task_12 = request.POST.get('task_12')

        try:
            project = Project.objects.get(id=pro_id)
            if project.Student:
                return redirect('e_project')
            
            student = Student.objects.get(id=stu_id)


            if(not project.Task_1):
                project.Student = student
                project.save()

                body = 'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                subject = "CREDEMA Projects - Project Allocation"

                send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                return redirect("e_project")
            else:
                if(task_1):
                    if project.Student_1:
                        return redirect('e_project')
                    
                    project.Student_1 = student
                    project.save()

                    body = 'Task:'+ project.Task_1 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_2):
                    if project.Student_2:
                        return redirect('e_project')
                    project.Student_2 = student
                    project.save()

                    body = 'Task:'+ project.Task_2 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_3):
                    if project.Student_3:
                        return redirect('e_project')
                    project.Student_3 = student
                    project.save()

                    body = 'Task:'+ project.Task_3 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_4):
                    if project.Student_4:
                        return redirect('e_project')
                    project.Student_4 = student
                    project.save()

                    body = 'Task:'+ project.Task_4 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_5):
                    if project.Student_5:
                        return redirect('e_project')
                    project.Student_5 = student
                    project.save()

                    body = 'Task:'+ project.Task_5 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_6):
                    if project.Student_6:
                        return redirect('e_project')
                    project.Student_6 = student
                    project.save()

                    body = 'Task:'+ project.Task_6 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_7):
                    if project.Student_7:
                        return redirect('e_project')
                    project.Student_7 = student
                    project.save()

                    body = 'Task:'+ project.Task_7 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_8):
                    if project.Student_8:
                        return redirect('e_project')
                    project.Student_8 = student
                    project.save()

                    body = 'Task:'+ project.Task_8 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_9):
                    if project.Student_9:
                        return redirect('e_project')
                    project.Student_9 = student
                    project.save()

                    body = 'Task:'+ project.Task_9 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_10):
                    if project.Student_10:
                        return redirect('e_project')
                    project.Student_10 = student
                    project.save()

                    body = 'Task:'+ project.Task_10 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_11):
                    if project.Student_11:
                        return redirect('e_project')
                    project.Student_11 = student
                    project.save()

                    body = 'Task:'+ project.Task_11 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
                elif(task_12):
                    if project.Student_12:
                        return redirect('e_project')
                    project.Student_12 = student
                    project.save()

                    body = 'Task:'+ project.Task_12 + ' of ' +'Project: '+project.Name + ' is allocated to you. Hope! you will work on it properly and finish it before given deadline.'
                    subject = "CREDEMA Projects - Task Allocation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect("e_project")
                
        except:
            return redirect("e_project")