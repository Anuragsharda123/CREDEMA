from django.shortcuts import render, redirect
from django.http import HttpRequest
from home.models.project import Project
from home.models.company import Company
from home.models.employe import Employe
from django.views import View
import json

class AddProject(View):
    def get(self, request):
        company = Company.objects.all()
        data={}
        # try:
        empid = request.session['employee']
        
        emp = Employe.objects.get(id=empid)

        data['company'] = company
        data['employee'] = emp
            
        return render(request, "add_project.html", data)
        # except:
        #     return redirect('e_login')
    

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

        if not error_message:
            project.save()
            return redirect('e_login')

        else:
            data = {
                'error': error_message
            }
        return render(request,'add_project.html', data)