from django.shortcuts import render, redirect
from home.models.project import Project
from home.models.company import Company
from home.models.employe import Employe
from datetime import datetime
from django.views import View


class AddProject(View):
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
        stipend = None
        name = request.POST.get('name')
        detail = request.FILES['detail']
        perk = request.POST.get('perk').lower()
        description = request.POST.get('description')
        if(request.POST.get('stipend')):
            stipend = int(request.POST.get('stipend'))
        duration = request.POST.get('duration')
        comp = request.POST.get('company')
        error_message = None

        skills = request.POST.getlist('skill')
        sk = ""

        for i in skills:
            if(not len(sk)):
                sk = sk+i
            else:
                sk = sk + ", " + i
        
        skill = sk.lower()

        empid = request.session['employee']
        emp = Employe.objects.get(id=empid)

        company = Company.objects.get(id=comp)

        project = Project(Name=name, Employe=emp, Project=detail, Skill_req=skill,
                          Description=description, Duration=duration, Perks=perk, Stipend=stipend, Company=company)
        
        isExist = Project.objects.filter(Project=detail)
        if isExist:
            error_message = "Project Already Exists"
        
        # if (det[-4:]) != '.pdf':
        #     error_message = "Only .pdf files are accepted"

        if(datetime.strptime(duration, "%Y-%m-%d")<datetime.today()):
            error_message = "Enter Valid Deadline"
        
        if(datetime.strptime(duration, "%Y-%m-%d")==datetime.today()):
            error_message = "Atleast one day is required to complete a task"

        if(stipend):
            if(stipend<5000):
                error_message = "Stipend should be more then or equal to ₹5000"

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