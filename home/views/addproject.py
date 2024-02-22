from django.shortcuts import render, redirect
from home.models.project import Project
from home.models.company import Company
from home.models.employe import Employe
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
        name = request.POST.get('name')
        skill = request.POST.get('skill').lower()
        detail = request.POST.get('detail')
        perk = request.POST.get('perk').lower()
        description = request.POST.get('description')
        stipend = request.POST.get('stipend')
        duration = request.POST.get('duration')
        comp = request.POST.get('company')

        error_message = None

        empid = request.session['employee']
        emp = Employe.objects.get(id=empid)

        company = Company.objects.get(id=comp)

        project = Project(Name=name, Employe=emp, Project=detail, Skill_req=skill,
                          Description=description, Duration=duration, Perks=perk, Stipend=stipend, Company=company)
        
        isExist = Project.objects.filter(Project=detail)
        if isExist:
            error_message = "Project Already Exists"
        
        if detail[-4:] != '.pdf':
            error_message = "Only .pdf files are accepted"

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