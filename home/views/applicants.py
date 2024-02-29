from django.shortcuts import render, redirect
from home.models.applicant import Applicant
from home.models.project import Project
from home.models.employe import Employe
from home.models.student import Student
from home.models.task_applicant import TaskApplicant
from django.views import View


class Applicants(View):
    def get(self, request):  
        return redirect('e_login')


    def post(self, request):
        try:
            if request.session['employee']:
                pro_id = request.POST.get('pro_id')
                project = Project.objects.get(id=pro_id)

                emp_id = request.session['employee']
                employe = Employe.objects.get(id=emp_id)

                students = []
                students_1 = []
                students_2 = []
                students_3 = []
                students_4 = []
                students_5 = []
                students_6 = []
                students_7 = []
                students_8 = []
                students_9 = []
                students_10 = []
                students_11 = []
                students_12 = []

                if project.Student:
                    return redirect('e_project')
                
                if(not project.Task_1):
                    application = Applicant.objects.filter(Project=project).values_list('Student')
                    
                    for i in application:
                        stu_id = i[0]
                        students.append(Student.objects.get(id=stu_id))

                else:
                    application_1 = TaskApplicant.objects.filter(Project=project, Task_1=True).values_list('Student')
                    for i in application_1:
                        stu_id = i[0]
                        students_1.append(Student.objects.get(id=stu_id))

                    application_2 = TaskApplicant.objects.filter(Project=project, Task_2=True).values_list('Student')
                    for i in application_2:
                        stu_id = i[0]
                        students_2.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_3):
                        application_3 = TaskApplicant.objects.filter(Project=project, Task_3=True).values_list('Student')
                        for i in application_3:
                            stu_id = i[0]
                            students_3.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_4):
                        application_4 = TaskApplicant.objects.filter(Project=project, Task_4=True).values_list('Student')
                        for i in application_4:
                            stu_id = i[0]
                            students_4.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_5):
                        application_5 = TaskApplicant.objects.filter(Project=project, Task_5=True).values_list('Student')
                        for i in application_5:
                            stu_id = i[0]
                            students_5.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_6):
                        application_6 = TaskApplicant.objects.filter(Project=project, Task_6=True).values_list('Student')
                        for i in application_6:
                            stu_id = i[0]
                            students_6.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_7):
                        application_7 = TaskApplicant.objects.filter(Project=project, Task_7=True).values_list('Student')
                        for i in application_7:
                            stu_id = i[0]
                            students_7.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_8):
                        application_8 = TaskApplicant.objects.filter(Project=project, Task_8=True).values_list('Student')
                        for i in application_8:
                            stu_id = i[0]
                            students_8.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_9):
                        application_9 = TaskApplicant.objects.filter(Project=project, Task_9=True).values_list('Student')
                        for i in application_9:
                            stu_id = i[0]
                            students_9.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_10):
                        application_10 = TaskApplicant.objects.filter(Project=project, Task_10=True).values_list('Student')
                        for i in application_10:
                            stu_id = i[0]
                            students_10.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_11):
                        application_11 = TaskApplicant.objects.filter(Project=project, Task_11=True).values_list('Student')
                        for i in application_11:
                            stu_id = i[0]
                            students_11.append(Student.objects.get(id=stu_id))
                    
                    if(project.Task_12):
                        application_12 = TaskApplicant.objects.filter(Project=project, Task_12=True).values_list('Student')
                        for i in application_12:
                            stu_id = i[0]
                            students_12.append(Student.objects.get(id=stu_id))
                    
                                    
                data = {}

                data['students'] = students
                data['students_1'] = students_1
                data['students_2'] = students_2
                data['students_3'] = students_3
                data['students_4'] = students_4
                data['students_5'] = students_5
                data['students_6'] = students_6
                data['students_7'] = students_7
                data['students_8'] = students_8
                data['students_9'] = students_9
                data['students_10'] = students_10
                data['students_11'] = students_11
                data['students_12'] = students_12
                data['project'] = project
                data['employe'] = employe

                return render(request, 'p_applicant.html', data)
        except:
            return redirect('e_login')