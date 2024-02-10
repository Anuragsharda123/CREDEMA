from django.shortcuts import redirect, render
from home.models.student import Student
from home.models.project import Project
from home.models.employe import Employe
from django.views import View

class Studentinfo(View):
    def get(self, request):
        return redirect('e_project')

    def post(self,request):
        emp_id = request.session['employee']
        stu_id = request.POST.get('stu_id')
        pro_id = request.POST.get('pro_id')
        
        data = {}

        student = Student.objects.get(id=stu_id)
        employe = Employe.objects.get(id=emp_id)
        project = Project.objects.get(id=pro_id)
        Name = student.Name.capitalize()
        skill = student.Skills.split(',')
        project = student.Projects.split(',')
        
        for i in range(0,len(skill)):
            w = skill[i].lstrip(" ")
            skill[i] = w.capitalize()

        for j in range(0,len(project)):
            p = project[j].lstrip(" ")
            project[j] = p.capitalize()

        data['student'] = student
        data['project'] = project
        data['employe'] = employe
        data['Name'] = Name
        data['skill'] = skill
        data['project'] = project
        # print(project)

        return render(request, 's_info.html', data)
    






    # <div id="skill" style="margin-left: 3vw;">
    #             <b>Skill(s) Required</b>
    #                 <ul>
    #                 {% for skill in skill %}
    #                     <li>{{skill}}</li>
    #                 {% endfor %}
                        
    #                 </ul>
    #         </div>