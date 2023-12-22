from django.shortcuts import render, redirect
from django.views import View
from home.models.project import Project

class Description(View):
    def get(self, request):
        try:
            if request.session['employee']:
                return redirect('e_project')
        except:
            return redirect('e_login')
        
    
    def post(self, request):
        pro_id = request.POST.get('pro_id')
        applied = None
        project = Project.objects.get(id = pro_id)
        data = {}
        skill = project.Skill_req.split(',')
        perk = project.Perks.split(',')
        description = project.Description.split('.')
        


        for i in range(0,len(skill)):
            w = skill[i].lstrip(" ")
            skill[i] = w

        for i in range(0,len(perk)):
            w = perk[i].lstrip(" ")
            perk[i] = w
            
        for i in range(0,len(description)):
            w = description[i].lstrip(" ")
            description[i] = w

        data['project'] = project
        data['perk'] = perk
        data['skill'] = skill
        data['description'] = description
        data['applied'] = applied

        return render(request, 'e_p_description.html', data)
