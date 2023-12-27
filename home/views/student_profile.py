from django.shortcuts import render, redirect
from home.models.student import Student
from django.views import View


class Studentprofile(View):
    def get(self, request):
        try:
            if request.session['student']:
                stu_id = request.session['student']
                student = Student.objects.get(id=stu_id)
                data = {}
                Name = student.Name.capitalize()
                skill = student.Skills.split(',')
                
                for i in range(0,len(skill)):
                    w = skill[i].lstrip(" ")
                    skill[i] = w.capitalize()

                data['student'] = student
                data['Name'] = Name
                data['skill'] = skill

                return render(request, 'student_profile.html',data)
        except:
            return redirect('s_login')