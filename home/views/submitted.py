from django.shortcuts import render,redirect
from home.models.employe import Employe
from home.models.project import Project
from django.views import View

class SubmittedProject(View):
    def get(self, request):
        try:
            emp = request.session['employee']
            employe = Employe.objects.get(id=emp)
            projects = Project.objects.filter(Employe=employe, Status='True')
            data = {}

            data['projects'] = projects
            data['employe'] = employe

            return render(request, 'submitted.html', data)
        except:
            return redirect('e_login')