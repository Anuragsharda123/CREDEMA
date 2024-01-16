from django.shortcuts import render, redirect
from django.views import View
from home.models.applicant import Applicant
from home.models.student import Student
from home.models.project import Project

class Description(View):
    def get(self, request):

        try:
            if request.session['student']:
                return redirect('home')
            
        except:
            try:
                if request.session['employee']:
                    return redirect('s_project')
            except:
                return redirect('s_login')
        
    
    def post(self, request):
        try:
            if request.session['student']:
                pro_id = request.POST.get('pro_id')
                applied = None
                project = Project.objects.get(id = pro_id)
                data = {}
                skill = project.Skill_req.split(',')
                perk = project.Perks.split(',')
                description = project.Description.split('.')
                

                try:
                    stu = request.session['student']
                    student = Student.objects.get(id=stu)
                    
                    if Applicant.objects.get(Student=student, Project=project):
                        applied = True
                
                except:
                    pass

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
                data['student'] = student

                return render(request, 'p_description.html', data)
        except:
            return redirect('home')