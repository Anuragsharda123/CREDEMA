from django.shortcuts import render, redirect
from home.models.company import Company
from home.models.employe import Employe
from home.models.project import Project
from datetime import datetime
from django.views import View

class Updateproject(View):
    def post(self, request):
        if request.POST.get('meth')=='get':
            # try:
            if request.session['employee']:
                pro_id = request.POST.get('update')
                company = Company.objects.all()
                project = Project.objects.get(id=pro_id)
                emp_id = request.session['employee']
                employe = Employe.objects.get(id=emp_id)

                data = {}

                data['project'] = project
                data['company'] = company
                data['employe'] = employe

                return render(request, 'updatepro.html', data)
            # except:
            #     return redirect('e_login')
            
        if request.POST.get('meth')=='post':
            name = request.POST.get('name')
            skill = request.POST.get('skill').lower()
            detail = request.POST.get('detail')
            perk = request.POST.get('perk').lower()
            description = request.POST.get('description')
            stipend = request.POST.get('stipend')
            duration = request.POST.get('duration')
            status = int(request.POST.get('status'))
            pro_id = request.POST.get('pro_id')
            last_update = datetime.today()
            
            project = Project.objects.get(id=pro_id)

            project.Name = name
            project.Perks = perk
            project.Skill_req = skill
            project.Stipend = stipend
            project.Status = status
            project.Last_update = last_update
        
            if detail:
                project.Project = detail
            
            if description:
                project.Description = description
        
            if duration:
                project.Duration = duration
        

            project.save()

            return redirect('e_project')