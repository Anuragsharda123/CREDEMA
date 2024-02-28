from django.shortcuts import render, redirect
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
        try:
            error_message = None
            description = request.POST.get('description')
            status = int(request.POST.get('status'))

            description_1 = request.POST.get('description_1')
            duration_1 = request.POST.get('duration_1')
            
            description_2 = request.POST.get('description_2')
            duration_2 = request.POST.get('duration_2')

            task_3 = None
            duration_3 = None
            stipend_3 = None

            task_4 = None
            duration_4 = None
            stipend_4 = None

            task_5 = None
            duration_5 = None
            stipend_5 = None

            task_6 = None
            duration_6 = None
            stipend_6 = None

            task_7 = None
            duration_7 = None
            stipend_7 = None

            task_8 = None
            duration_8 = None
            stipend_8 = None

            task_9 = None
            duration_9 = None
            stipend_9 = None

            task_10 = None
            duration_10 = None
            stipend_10 = None

            task_11 = None
            duration_11 = None
            stipend_11 = None

            task_12 = None
            duration_12 = None
            stipend_12 = None
            
            if(request.POST.get('task_3')):
                task_3 = request.POST.get('task_3')
            description_3 = request.POST.get('description_3')
            if(request.POST.get('stipend_3')):
                stipend_3 = request.POST.get('stipend_3')
            if(request.POST.get('duration_3')):
                duration_3 = request.POST.get('duration_3')

            if(request.POST.get('task_4')):
                task_4 = request.POST.get('task_4')
            description_4 = request.POST.get('description_4')
            if(request.POST.get('stipend_4')):
                stipend_4 = request.POST.get('stipend_4')
            if(request.POST.get('duration_4')):
                duration_4 = request.POST.get('duration_4')
            
            if(request.POST.get('task_5')):
                task_5 = request.POST.get('task_5')
            description_5 = request.POST.get('description_5')
            if(request.POST.get('stipend_5')):
                stipend_5 = request.POST.get('stipend_5')
            if(request.POST.get('duration_5')):
                duration_5 = request.POST.get('duration_5')
            
            if(request.POST.get('task_6')):
                task_6 = request.POST.get('task_6')
            description_6 = request.POST.get('description_6')
            if(request.POST.get('stipend_6')):
                stipend_6 = request.POST.get('stipend_6')
            if(request.POST.get('duration_6')):
                duration_6 = request.POST.get('duration_6')
            
            if(request.POST.get('task_7')):
                task_7 = request.POST.get('task_7')
            description_7 = request.POST.get('description_7')
            if(request.POST.get('stipend_7')):
                stipend_7 = request.POST.get('stipend_7')
            if(request.POST.get('duration_7')):
                duration_7 = request.POST.get('duration_7')

            if(request.POST.get('task_8')):
                task_8 = request.POST.get('task_8')
            description_8 = request.POST.get('description_8')
            if(request.POST.get('stipend_8')):
                stipend_8 = request.POST.get('stipend_8')
            if(request.POST.get('duration_8')):
                duration_8 = request.POST.get('duration_8')
            
            if(request.POST.get('task_9')):
                task_9 = request.POST.get('task_9')
            description_9 = request.POST.get('description_9')
            if(request.POST.get('stipend_9')):
                stipend_9 = request.POST.get('stipend_9')
            if(request.POST.get('duration_9')):
                duration_9 = request.POST.get('duration_9')
            
            if(request.POST.get('task_10')):
                task_10 = request.POST.get('task_10')
            description_10 = request.POST.get('description_10')
            if(request.POST.get('stipend_10')):
                stipend_10 = request.POST.get('stipend_10')
            if(request.POST.get('duration_10')):
                duration_10 = request.POST.get('duration_10')

            if(request.POST.get('task_11')):
                task_11 = request.POST.get('task_11')
            description_11 = request.POST.get('description_11')
            if(request.POST.get('stipend_11')):
                stipend_11 = request.POST.get('stipend_11')
            if(request.POST.get('duration_11')):
                duration_11 = request.POST.get('duration_11')
            
            if(request.POST.get('task_12')):
                task_12 = request.POST.get('task_12')
            description_12 = request.POST.get('description_12')
            if(request.POST.get('stipend_12')):
                stipend_12 = request.POST.get('stipend_12')
            if(request.POST.get('duration_12')):
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
                if (duration_1>project.Duration_1):
                    project.Duration_1 = duration_1
                
            if(description_2):
                project.Description_2 = description_2
            if(duration_2):
                dur = duration_2.split('-')
                duration_2 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                if duration_2>project.Duration_2:
                    project.Duration_2 = duration_2

            if(task_3):
                if(project.Task_3):
                    if(project.Task_3):
                        if(description_3):
                            project.Description_3 = description_3
                        if(duration_3):
                            dur = duration_3.split('-')
                            duration_3 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_3):
                                if duration_3>project.Duration_3:
                                    project.Duration_3 = duration_3
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_3 or description_3 or stipend_3 or duration_3):
                    if(task_3):
                        project.Task_3 = task_3
                        if(description_3):
                            project.Description_3 = description_3
                            if(stipend_3):
                                project.Stipend_3 = stipend_3
                                if(duration_3):
                                    project.Duration_3 = duration_3
                                else:
                                    error_message = "Please provide all information for Task 3"
                        else:
                            error_message = "Please provide all information for Task 3"
                    else:
                        error_message = "Please provide all information for Task 3"

            if(task_4):
                if(project.Task_4):
                    if(project.Task_4):
                        if(description_4):
                            project.Description_4 = description_4
                        if(duration_4):
                            dur = duration_4.split('-')
                            duration_4 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_4):
                                if duration_4>project.Duration_4:
                                    project.Duration_4 = duration_4
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_4 or description_4 or stipend_4 or duration_4):
                    if(task_4):
                        project.Task_4 = task_4
                        if(description_4):
                            project.Description_4 = description_4
                            if(stipend_4):
                                project.Stipend_4 = stipend_4
                                if(duration_4):
                                    project.Duration_4 = duration_4
                                else:
                                    error_message = "Please provide all information for Task 4"
                        else:
                            error_message = "Please provide all information for Task 4"
                    else:
                        error_message = "Please provide all information for Task 4"
                
            if(task_5):
                if(project.Task_5):
                    if(project.Task_5):
                        if(description_5):
                            project.Description_5 = description_5
                        if(duration_5):
                            dur = duration_5.split('-')
                            duration_5 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_5):
                                if duration_5>project.Duration_5:
                                    project.Duration_5 = duration_5
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_5 or description_5 or stipend_5 or duration_5):
                    if(task_5):
                        project.Task_5 = task_5
                        if(description_5):
                            project.Description_5 = description_5
                            if(stipend_5):
                                project.Stipend_5 = stipend_5
                                if(duration_5):
                                    project.Duration_5 = duration_5
                                else:
                                    error_message = "Please provide all information for Task 5"
                        else:
                            error_message = "Please provide all information for Task 5"
                    else:
                        error_message = "Please provide all information for Task 5"
                
            if(task_6):
                if(project.Task_6):
                    if(project.Task_6):
                        if(description_6):
                            project.Description_6 = description_6
                        if(duration_6):
                            dur = duration_6.split('-')
                            duration_6 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_6):
                                if duration_6>project.Duration_6:
                                    project.Duration_6 = duration_6
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_6 or description_6 or stipend_6 or duration_6):
                    if(task_6):
                        project.Task_6 = task_6
                        if(description_6):
                            project.Description_6 = description_6
                            if(stipend_6):
                                project.Stipend_6 = stipend_6
                                if(duration_6):
                                    project.Duration_6 = duration_6
                                else:
                                    error_message = "Please provide all information for Task 6"
                        else:
                            error_message = "Please provide all information for Task 6"
                    else:
                        error_message = "Please provide all information for Task 6"
                
            if(task_7):
                if(project.Task_7):
                    if(project.Task_7):
                        if(description_7):
                            project.Description_7 = description_7
                        if(duration_7):
                            dur = duration_7.split('-')
                            duration_7 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_7):
                                if duration_7>project.Duration_7:
                                    project.Duration_7 = duration_7
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_7 or description_7 or stipend_7 or duration_7):
                    if(task_7):
                        project.Task_7 = task_7
                        if(description_7):
                            project.Description_7 = description_7
                            if(stipend_7):
                                project.Stipend_7 = stipend_7
                                if(duration_7):
                                    project.Duration_7 = duration_7
                                else:
                                    error_message = "Please provide all information for Task 7"
                        else:
                            error_message = "Please provide all information for Task 7"
                    else:
                        error_message = "Please provide all information for Task 7"
                
            if(task_8):
                if(project.Task_8):
                    if(project.Task_8):
                        if(description_8):
                            project.Description_8 = description_8
                        if(duration_8):
                            dur = duration_8.split('-')
                            duration_8 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_8):
                                if duration_8>project.Duration_8:
                                    project.Duration_8 = duration_8
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_8 or description_8 or stipend_8 or duration_8):
                    if(task_8):
                        project.Task_8 = task_8
                        if(description_8):
                            project.Description_8 = description_8
                            if(stipend_8):
                                project.Stipend_8 = stipend_8
                                if(duration_8):
                                    project.Duration_8 = duration_8
                                else:
                                    error_message = "Please provide all information for Task 8"
                        else:
                            error_message = "Please provide all information for Task 8"
                    else:
                        error_message = "Please provide all information for Task 8"
                
            if(task_9):
                if(project.Task_9):
                    if(project.Task_9):
                        if(description_9):
                            project.Description_9 = description_9
                        if(duration_9):
                            dur = duration_9.split('-')
                            duration_9 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_9):
                                if duration_9>project.Duration_9:
                                    project.Duration_9 = duration_9
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_9 or description_9 or stipend_9 or duration_9):
                    if(task_9):
                        project.Task_9 = task_9
                        if(description_9):
                            project.Description_9 = description_9
                            if(stipend_9):
                                project.Stipend_9 = stipend_9
                                if(duration_9):
                                    project.Duration_9 = duration_9
                                else:
                                    error_message = "Please provide all information for Task 9"
                        else:
                            error_message = "Please provide all information for Task 9"
                    else:
                        error_message = "Please provide all information for Task 9"
                
            if(task_10):
                if(project.Task_10):
                    if(project.Task_10):
                        if(description_10):
                            project.Description_10 = description_10
                        if(duration_10):
                            dur = duration_10.split('-')
                            duration_10 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_10):
                                if duration_10>project.Duration_10:
                                    project.Duration_10 = duration_10
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_10 or description_10 or stipend_10 or duration_10):
                    if(task_10):
                        project.Task_10 = task_10
                        if(description_10):
                            project.Description_10 = description_10
                            if(stipend_10):
                                project.Stipend_10 = stipend_10
                                if(duration_10):
                                    project.Duration_10 = duration_10
                                else:
                                    error_message = "Please provide all information for Task 10"
                            else:
                                error_message = "Please provide all information for Task 10"
                        else:
                            error_message = "Please provide all information for Task 10"
                    else:
                        error_message = "Please provide all information for Task 10"
                
            if(task_11):
                if(project.Task_11):
                    if(project.Task_11):
                        if(description_11):
                            project.Description_11 = description_11
                        if(duration_11):
                            dur = duration_11.split('-')
                            duration_11 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_11):
                                if duration_11>project.Duration_11:
                                    project.Duration_11 = duration_11
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_11 or description_11 or stipend_11 or duration_11):
                    if(task_11):
                        project.Task_11 = task_11
                        if(description_11):
                            project.Description_11 = description_11
                            if(stipend_11):
                                project.Stipend_11 = stipend_11
                                if(duration_11):
                                    project.Duration_11 = duration_11
                                else:
                                    error_message = "Please provide all information for Task 11"
                            else:
                                error_message = "Please provide all information for Task 11"
                        else:
                            error_message = "Please provide all information for Task 11"
                    else:
                        error_message = "Please provide all information for Task 11"
                
            if(task_12):
                if(project.Task_12):
                    if(project.Task_12):
                        if(description_12):
                            project.Description_12 = description_12
                        if(duration_12):
                            dur = duration_12.split('-')
                            duration_12 = date(int(dur[0]), int(dur[1]), int(dur[2]))
                            if(project.Duration_12):
                                if duration_12>project.Duration_12:
                                    project.Duration_12 = duration_12
                                else:
                                    error_message = "You are not allowed to decrease the deadline"
                elif(task_12 or description_12 or stipend_12 or duration_12):
                    if(task_12):
                        project.Task_12 = task_12
                        if(description_12):
                            project.Description_12 = description_12
                            if(stipend_12):
                                project.Stipend_12 = stipend_12
                                if(duration_12):
                                    project.Duration_12 = duration_12
                                else:
                                    error_message = "Please provide all information for Task 12"
                            else:
                                error_message = "Please provide all information for Task 12"
                        else:
                            error_message = "Please provide all information for Task 12"
                    else:
                        error_message = "Please provide all information for Task 12"
        

            if (error_message):
                # data = {
                #     "error":error_message,
                #     "product": project
                # }
                return redirect('e_project')

            project.save()
            try:
                if(project.Student):
                    stu = project.Student
                    student = Student.objects.get(Email=stu)
                            

                    body = 'Project: '+project.Name + " is Updated. Check the project details again and if updations are not suitable to you than contact to your TPO or CREDEMA."
                    subject = "CREDEMA Projects - Project Updation"

                    send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])

                    return redirect('e_project')
                
            except:
                return redirect('e_project')    
            
            return redirect('e_project')
        except:
            return redirect('e_project')
            