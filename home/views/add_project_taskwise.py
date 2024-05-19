from django.shortcuts import render, redirect
from home.models.project import Project
from home.models.company import Company
from home.models.employe import Employe
from datetime import datetime
from django.views import View


class AddProjectTask(View):
    def get(self, request):

        try:
            if request.session['employee']:
                company = Company.objects.all()
                data={}
                # try:
                empid = request.session['employee']
                
                employe = Employe.objects.get(id=empid)

                data['company'] = company
                data['employee'] = employe
                data['employe'] = employe
                    
                return render(request, "add_project.html", data)
        except:
            return redirect('e_login')
    

    def post(self, request):
        stipend_3 = 1000
        stipend_4 = 1000
        stipend_5 = 1000
        stipend_6 = 1000
        stipend_7 = 1000
        stipend_8 = 1000
        stipend_9 = 1000
        stipend_10 = 1000
        stipend_11 = 1000
        stipend_12 = 1000

        duration_3 = None
        duration_4 = None
        duration_5 = None
        duration_6 = None
        duration_7 = None
        duration_8 = None
        duration_9 = None
        duration_10 = None
        duration_11 = None
        duration_12 = None

        name = request.POST.get('name')
        comp = request.POST.get('company')
        det = request.POST.get('detail')
        detail = request.FILES['detail']
        description = request.POST.get('description')
        perk = request.POST.get('perk').lower()

        skills = request.POST.getlist('skill')
        sk = ""

        for i in skills:
            if(not len(sk)):
                sk = sk+i
            else:
                sk = sk + ", " + i
        
        skill = sk.lower()
        
        task_1 = request.POST.get('task_1')
        description_1 = request.POST.get('description_1')
        stipend_1 = int(request.POST.get('stipend_1'))
        duration_1 = request.POST.get('duration_1')

        task_2 = request.POST.get('task_2')
        description_2 = request.POST.get('description_2')
        stipend_2= int(request.POST.get('stipend_2'))
        duration_2 = request.POST.get('duration_2')

        task_3 = request.POST.get('task_3')
        description_3 = request.POST.get('description_3')
        if(request.POST.get('stipend_3')):
            stipend_3 = request.POST.get('stipend_3')
        if(request.POST.get('duration_3')):
            duration_3 = request.POST.get('duration_3')

        task_4 = request.POST.get('task_4')
        description_4 = request.POST.get('description_4')
        if(request.POST.get('stipend_4')):
            stipend_4 = request.POST.get('stipend_4')
        if(request.POST.get('duration_4')):
            duration_4 = request.POST.get('duration_4')

        task_5 = request.POST.get('task_5')
        description_5 = request.POST.get('description_5')
        if(request.POST.get('stipend_5')):
            stipend_5 = request.POST.get('stipend_5')
        if(request.POST.get('duration_5')):
            duration_5 = request.POST.get('duration_5')

        task_6 = request.POST.get('task_6')
        description_6 = request.POST.get('description_6')
        if(request.POST.get('stipend_6')):
            stipend_6 = request.POST.get('stipend_6')
        if(request.POST.get('duration_6')):
            duration_6 = request.POST.get('duration_6')

        task_7 = request.POST.get('task_7')
        description_7 = request.POST.get('description_7')
        if(request.POST.get('stipend_7')):
            stipend_7 = request.POST.get('stipend_7')
        if(request.POST.get('duration_7')):
            duration_7 = request.POST.get('duration_7')

        task_8 = request.POST.get('task_8')
        description_8 = request.POST.get('description_8')
        if(request.POST.get('stipend_8')):
            stipend_8 = request.POST.get('stipend_8')
        if(request.POST.get('duration_8')):
            duration_8 = request.POST.get('duration_8')

        task_9 = request.POST.get('task_9')
        description_9 = request.POST.get('description_9')
        if(request.POST.get('stipend_9')):
            stipend_9 = request.POST.get('stipend_9')
        if(request.POST.get('duration_9')):
            duration_9 = request.POST.get('duration_9')

        task_10 = request.POST.get('task_10')
        description_10 = request.POST.get('description_10')
        if(request.POST.get('stipend_10')):
            stipend_10 = request.POST.get('stipend_10')
        if(request.POST.get('duration_10')):
            duration_10 = request.POST.get('duration_10')

        task_11 = request.POST.get('task_11')
        description_11 = request.POST.get('description_11')
        if(request.POST.get('stipend_11')):
                stipend_11 = request.POST.get('stipend_11')
        if(request.POST.get('duration_11')):
            duration_11 = request.POST.get('duration_11')

        task_12 = request.POST.get('task_12')
        description_12 = request.POST.get('description_12')
        if(request.POST.get('stipend_12')):
            stipend_12 = request.POST.get('stipend_12')
        if(request.POST.get('duration_12')):
            duration_12 = request.POST.get('duration_12')

        error_message = None

        empid = request.session['employee']
        emp = Employe.objects.get(id=empid)

        company = Company.objects.get(id=comp)

        project = Project(Name=name, Employe=emp, Project=detail, Skill_req=skill,
                          Description=description, Perks=perk, Company=company, 
                          Task_1=task_1, Description_1=description_1, Stipend_1=stipend_1, Duration_1=duration_1,
                          Task_2=task_2, Description_2=description_2, Stipend_2=stipend_2, Duration_2=duration_2,
                          Task_3=task_3, Description_3=description_3, Stipend_3=stipend_3, Duration_3=duration_3,
                          Task_4=task_4, Description_4=description_4, Stipend_4=stipend_4, Duration_4=duration_4,
                          Task_5=task_5, Description_5=description_5, Stipend_5=stipend_5, Duration_5=duration_5,
                          Task_6=task_6, Description_6=description_6, Stipend_6=stipend_6, Duration_6=duration_6,
                          Task_7=task_7, Description_7=description_7, Stipend_7=stipend_7, Duration_7=duration_7,
                          Task_8=task_8, Description_8=description_8, Stipend_8=stipend_8, Duration_8=duration_8,
                          Task_9=task_9, Description_9=description_9, Stipend_9=stipend_9, Duration_9=duration_9,
                          Task_10=task_10, Description_10=description_10, Stipend_10=stipend_10, Duration_10=duration_10,
                          Task_11=task_11, Description_11=description_11, Stipend_11=stipend_11, Duration_11=duration_11,
                          Task_12=task_12, Description_12=description_12, Stipend_12=stipend_12, Duration_12=duration_12)
        
        isExist = Project.objects.filter(Project=detail)
        if isExist:
            error_message = "Project Already Exists"
        
        if det[-4:] != '.pdf':
            error_message = "Only .pdf files are accepted"

        if (int(stipend_1)<1000):
            error_message = "Task 1 stipend should be ₹1000 or more"

        if (int(stipend_2)<1000):
            error_message = "Task 2 stipend should be ₹1000 or more"

        if (int(stipend_3)<1000):
            error_message = "Task 3 stipend should be ₹1000 or more"

        if (int(stipend_4)<1000):
            error_message = "Task 4 stipend should be ₹1000 or more"

        if (int(stipend_5)<1000):
            error_message = "Task 5 stipend should be ₹1000 or more"

        if (int(stipend_6)<1000):
            error_message = "Task 6 stipend should be ₹1000 or more"

        if (int(stipend_7)<1000):
            error_message = "Task 7 stipend should be ₹1000 or more"

        if (int(stipend_8)<1000):
            error_message = "Task 8 stipend should be ₹1000 or more"

        if (int(stipend_9)<1000):
            error_message = "Task 9 stipend should be ₹1000 or more"

        if (int(stipend_10)<1000):
            error_message = "Task 10 stipend should be ₹1000 or more"

        if (int(stipend_11)<1000):
            error_message = "Task 11 stipend should be ₹1000 or more"

        if (int(stipend_12)<1000):
            error_message = "Task 12 stipend should be ₹1000 or more"

        if((datetime.strptime(duration_1, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_2, "%Y-%m-%d")<datetime.today())):
            error_message = "Enter Valid Deadline"
        
        if((datetime.strptime(duration_1, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_2, "%Y-%m-%d")==datetime.today())):
            error_message = "Atleast one day is required to complete a task"

        # if((duration_3) or (duration_4) or (duration_5) or (duration_6) or (duration_7) or (duration_8) or (duration_9) or (duration_10) or (duration_11) or (duration_12)):
        #     if((datetime.strptime(duration_3, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_4, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_5, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_6, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_7, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_8, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_9, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_10, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_11, "%Y-%m-%d")<datetime.today()) or (datetime.strptime(duration_12, "%Y-%m-%d")<datetime.today())):
        #         error_message = "Enter Valid Deadline"
            
        #     if((datetime.strptime(duration_3, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_4, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_5, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_6, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_7, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_8, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_9, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_10, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_11, "%Y-%m-%d")==datetime.today()) or (datetime.strptime(duration_12, "%Y-%m-%d")==datetime.today())):
        #         error_message = "Atleast one day is required to complete a task"


        if not error_message:
            project.save()
            return redirect('e_login')

        else:
            company = Company.objects.all()
            data = {
                'error': error_message,
                'company':company
            }
        return render(request,'add_project.html', data)