from django.shortcuts import render, redirect
from home.models.company import Company
from home.models.project import Project
from django.views import View

class Updateproduct(View):
    def get(self, request):
        pro_id = request.GET.get('update')
        company = Company.objects.all()
        project = Project.objects.get(id=pro_id)

        data = {}

        data['project'] = project
        data['company'] = company

        return render(request, 'updatepro.html', data)
    
    def post(self, request):
        name = request.POST.get('name')
        skill = request.POST.get('skill').lower()
        detail = request.POST.get('detail')
        perk = request.POST.get('perk').lower()
        description = request.POST.get('description')
        stipend = request.POST.get('stipend')
        duration = request.POST.get('duration')
        status = int(request.POST.get('status'))
        pro_id = request.POST.get('pro_id')
        
        project = Project.objects.get(id=pro_id)

        project.Name = name
        project.Perks = perk
        project.Skill_req = skill
        project.Stipend = stipend
        project.Status = status
    
        if detail:
            project.Project = detail
        
        if description:
            project.Description = description
    
        if duration:
            project.Duration = duration
    

        project.save()

        return redirect('e_project')