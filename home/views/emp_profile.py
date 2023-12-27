from django.shortcuts import render, redirect
from home.models.employe import Employe
from django.views import View


class Employeeprofile(View):
    def get(self, request):
        try:
            if request.session['employee']:
                emp_id = request.session['employee']
                employe = Employe.objects.get(id=emp_id)
                data = {}
                Name = employe.Name.capitalize()
                

                data['employe'] = employe
                data['Name'] = Name

                return render(request, 'emp_profile.html',data)
        except:
            return redirect('e_login')