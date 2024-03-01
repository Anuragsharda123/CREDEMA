from django.shortcuts import redirect, render
from home.models.student import Student
from home.models.project import Project
from home.models.employe import Employe
from django.views import View

class Studentinfo(View):
    def get(self, request):
        return redirect('e_project')

    def post(self,request):
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
        t_1 = False
        t_2 = False
        t_3 = False
        t_4 = False
        t_5 = False
        t_6 = False
        t_7 = False
        t_8 = False
        t_9 = False
        t_10 = False
        t_11 = False
        t_12 = False
        
        emp_id = request.session['employee']
        stu_id = request.POST.get('stu_id')
        pro_id = request.POST.get('pro_id')
        print("AAAAAA: ",request.POST.get('task_1'))
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


        print("Pro_id: ",pro_id)
        
        data = {}

        student = Student.objects.get(id=stu_id)
        employe = Employe.objects.get(id=emp_id)
        project = Project.objects.get(id=pro_id)

        if(task_1):
            t_1 = True

        elif(task_2):
            t_2 = True

        elif(task_3):
            t_3 = True

        elif(task_4):
            t_4 = True

        elif(task_5):
            t_5 = True

        elif(task_6):
            t_6 = True

        elif(task_7):
            t_7 = True

        elif(task_8):
            t_8 = True

        elif(task_9):
            t_9 = True

        elif(task_10):
            t_10 = True

        elif(task_11):
            t_11 = True

        elif(task_12):
            t_12 = True

        Name = student.Name.capitalize()
        skill = student.Skills.split(',')
        stuprojects = student.Projects.split(',')
        
        for i in range(0,len(skill)):
            w = skill[i].lstrip(" ")
            skill[i] = w.capitalize()

        for j in range(0,len(stuprojects)):
            p = stuprojects[j].lstrip(" ")
            stuprojects[j] = p.capitalize()

        data['student'] = student
        data['project'] = project
        data['employe'] = employe
        data['Name'] = Name
        data['skill'] = skill
        data['stuprojects'] = stuprojects
        data['task_1'] = t_1
        data['task_2'] = t_2
        data['task_3'] = t_3
        data['task_4'] = t_4
        data['task_5'] = t_5
        data['task_6'] = t_6
        data['task_7'] = t_7
        data['task_8'] = t_8
        data['task_9'] = t_9
        data['task_10'] = t_10
        data['task_11'] = t_11
        data['task_12'] = t_12
        print("PPP: ",project)

        return render(request, 's_info.html', data)
    
