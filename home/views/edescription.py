from django.shortcuts import render, redirect
from django.views import View
from home.models.student import Student
from home.models.employe import Employe
from home.models.project import Project

class Description(View):
    def get(self, request):
        try:
            if request.session['employee']:
                return redirect('e_project')
        except:
            return redirect('e_login')
        
    
    def post(self, request):
            if request.session['employee']:
                pro_id = request.POST.get('pro_id')
                applied = None
                project = Project.objects.get(id = pro_id)
                data = {}
                skill = project.Skill_req.split(',')
                perk = project.Perks.split(',')
                description = project.Description.split('.')
                emp_id = request.session['employee']
                employe = Employe.objects.get(id=emp_id)
                student = None
                student_1 = None
                student_2 = None
                student_3 = None
                student_4 = None
                student_5 = None
                student_6 = None
                student_7 = None
                student_8 = None
                student_9 = None
                student_10 = None
                student_11 = None
                student_12 = None

                if(project.Student):
                    student = Student.objects.get(Email=project.Student)

                if(project.Student_1):
                    student_1 = Student.objects.get(Email=project.Student_1)

                if(project.Student_2):
                    student_2 = Student.objects.get(Email=project.Student_2)

                if(project.Student_3):
                    student_3 = Student.objects.get(Email=project.Student_3)

                if(project.Student_4):
                    student_4 = Student.objects.get(Email=project.Student_4)

                if(project.Student_5):
                    student_5 = Student.objects.get(Email=project.Student_5)

                if(project.Student_6):
                    student_6 = Student.objects.get(Email=project.Student_6)

                if(project.Student_7):
                    student_7 = Student.objects.get(Email=project.Student_7)

                if(project.Student_8):
                    student_8 = Student.objects.get(Email=project.Student_8)

                if(project.Student_9):
                    student_9 = Student.objects.get(Email=project.Student_9)

                if(project.Student_10):
                    student_10 = Student.objects.get(Email=project.Student_10)

                if(project.Student_11):
                    student_11 = Student.objects.get(Email=project.Student_11)

                if(project.Student_12):
                    student_12 = Student.objects.get(Email=project.Student_12)


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
                data['employe'] = employe
                data['student']  = student
                data['student_1'] = student_1
                data['student_2'] = student_2
                data['student_3'] = student_3
                data['student_4'] = student_4
                data['student_5'] = student_5
                data['student_6'] = student_6
                data['student_7'] = student_7
                data['student_8'] = student_8
                data['student_9'] = student_9
                data['student_10'] = student_10
                data['student_11'] = student_11
                data['student_12'] = student_12

                return render(request, 'e_p_description.html', data)
            
        # except:
        #     return redirect('e_login')