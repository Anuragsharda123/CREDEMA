from django.shortcuts import render, redirect
from django.views import View
from home.models.student import Student
from home.models.project import Project

class S_T_Description(View):
    def get(self, request):
        try:
            if request.session['student']:
                return redirect('home')
        except:
            return redirect('login')
        
    
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
                stu_id = request.session['student']
                student = Student.objects.get(id=stu_id)
                stu = []

                for i in range(0,len(skill)):
                    w = skill[i].lstrip(" ")
                    skill[i] = w

                for i in range(0,len(perk)):
                    w = perk[i].lstrip(" ")
                    perk[i] = w
                    
                for i in range(0,len(description)):
                    w = description[i].lstrip(" ")
                    description[i] = w

                if (project.Student_1 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_2 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_3 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_4 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_5 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_6 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_7 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_8 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_9 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_10 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_11 == student):
                    stu.append(True)
                else:
                    stu.append(False)
                if (project.Student_12 == student):
                    stu.append(True)
                else:
                    stu.append(False)

                data['project'] = project
                data['perk'] = perk
                data['skill'] = skill
                data['description'] = description
                data['applied'] = applied
                data['student'] = student
                data['stu'] = stu

                return render(request, 's_t_description.html', data)
            
        except:
            return redirect('e_login')