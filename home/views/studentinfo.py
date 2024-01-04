from django.shortcuts import redirect, render
from home.models.student import Student
from django.views import View

class Studentinfo(View):
    def get(self, request):
        return redirect('e_project')

    def post(self,request):
        stu_id = request.POST.get('stu_id')
        pro_id = request.POST.get('pro_id')
        data = {}
        

        student = Student.objects.get(id=stu_id)
        Name = student.Name.capitalize()
        skill = student.Skills.split(',')
        
        for i in range(0,len(skill)):
            w = skill[i].lstrip(" ")
            skill[i] = w.capitalize()

        data['student'] = student
        data['Name'] = Name
        data['skill'] = skill
        # print(skill)

        return render(request, 's_info.html', data)
    






    # <div id="skill" style="margin-left: 3vw;">
    #             <b>Skill(s) Required</b>
    #                 <ul>
    #                 {% for skill in skill %}
    #                     <li>{{skill}}</li>
    #                 {% endfor %}
                        
    #                 </ul>
    #         </div>