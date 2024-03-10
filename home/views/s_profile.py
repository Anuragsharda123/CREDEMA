from django.shortcuts import render, redirect
from home.models.student import Student
from django.views import View


class S_profile(View):
    def post(self, request):
        try:
            if request.session['student']:
                student = request.session['student']
                stu_id = request.POST.get('stu_id')
                l_student = Student.objects.get(id=stu_id)
                data = {}
                Name = l_student.Name.capitalize()
                skill = l_student.Skills.split(',')
                projects = l_student.Projects.split(',')
                
                for i in range(0,len(skill)):
                    w = skill[i].lstrip(" ")
                    skill[i] = w.capitalize()

                for i in range(0,len(projects)):
                    w = projects[i].lstrip(" ")
                    projects[i] = w.capitalize()

                data['p_student'] = l_student
                data['Name'] = Name
                data['skill'] = skill
                data['student'] = student
                data['projects'] = projects

                return render(request, 's_profile.html',data)
        except:
            return redirect('s_login')