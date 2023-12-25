from django.shortcuts import render,redirect
from home.models.employe import Employe
from home.models.project import Project
from django.views import View

class EmployeProject(View):
    def get(self, request):
        try:
            emp = request.session['employee']
            employe = Employe.objects.get(id=emp)
            projects = Project.objects.filter(Employe=employe)
            data = {}

            data['projects'] = projects

            return render(request, 'e_project.html', data)
        except:
            return redirect('e_login')