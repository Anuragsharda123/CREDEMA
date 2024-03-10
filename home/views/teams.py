from django.shortcuts import render, redirect
from home.models.project import Project
from home.models.student import Student
from django.views import View

class Teams(View):
    def get(self, request):
        try:
            if(request.session['student']):
                pro = Project.objects.all()
                stu_id = request.session['student']
                stu = Student.objects.get(id=stu_id)
                projects = []

                for i in pro:
                    if ((stu == i.Student_1) or (stu == i.Student_2) or (stu == i.Student_3) or 
                        (stu == i.Student_4) or (stu == i.Student_5) or (stu == i.Student_6) or 
                        (stu == i.Student_7) or (stu == i.Student_8) or (stu == i.Student_9) or 
                        (stu == i.Student_10) or (stu == i.Student_11) or (stu == i.Student_12)):
                        projects.append(i)

                data = {}
                data['projects'] = projects
                data['student'] = stu
                
                return render(request, 'teams.html', data)
        except:
            return redirect('home')

    def post(self, request):
        pro_id = request.POST.get('pro_id')
        pro = Project.objects.get(id=pro_id)
        stu_id = request.session['student']
        student = Student.objects.get(id=stu_id)
        students = []
        task = []

        if(pro.Student_1):
            stu = Student.objects.get(Email=pro.Student_1)
            if(not (stu == student)):
                task.append(pro.Task_1)
                students.append(stu)

        if(pro.Student_2):
            stu = Student.objects.get(Email=pro.Student_2)
            if(not (stu == student)):
                task.append(pro.Task_2)
                students.append(stu)

        if(pro.Student_3):
            stu = Student.objects.get(Email=pro.Student_3)
            if(not (stu == student)):
                task.append(pro.Task_3)
                students.append(stu)

        if(pro.Student_4):
            stu = Student.objects.get(Email=pro.Student_4)
            if(not (stu == student)):
                task.append(pro.Task_4)
                students.append(stu)

        if(pro.Student_5):
            stu = Student.objects.get(Email=pro.Student_5)
            if(not (stu == student)):
                task.append(pro.Task_5)
                students.append(stu)

        if(pro.Student_6):
            stu = Student.objects.get(Email=pro.Student_6)
            if(not (stu == student)):
                task.append(pro.Task_6)
                students.append(stu)

        if(pro.Student_7):
            stu = Student.objects.get(Email=pro.Student_7)
            if(not (stu == student)):
                task.append(pro.Task_7)
                students.append(stu)

        if(pro.Student_8):
            stu = Student.objects.get(Email=pro.Student_8)
            if(not (stu == student)):
                task.append(pro.Task_8)
                students.append(stu)

        if(pro.Student_9):
            stu = Student.objects.get(Email=pro.Student_9)
            if(not (stu == student)):
                task.append(pro.Task_9)
                students.append(stu)

        if(pro.Student_10):
            stu = Student.objects.get(Email=pro.Student_10)
            if(not (stu == student)):
                task.append(pro.Task_10)
                students.append(stu)

        if(pro.Student_11):
            stu = Student.objects.get(Email=pro.Student_11)
            if(not (stu == student)):
                task.append(pro.Task_11)
                students.append(stu)

        if(pro.Student_12):
            stu = Student.objects.get(Email=pro.Student_12)
            if(not (stu == student)):
                task.append(pro.Task_12)
                students.append(stu)

        data = {}
        data['students'] = students
        data['student'] = student
        data['task'] = task
        data['project'] = pro
        
        return render(request, 'my_team.html', data)


