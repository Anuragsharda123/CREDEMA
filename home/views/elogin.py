from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from home.models.employe import Employe
from django.views import View

class EmployeeLogin(View):
    def get(self, request):
        try:
            if request.session['employee']:
                return redirect('e_project')
            
        except:

            return render(request, "e_login.html")
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            employee = Employe.objects.get(Email=email)
        except:
            employee = False

        error_message = None

        if employee:
            flag = check_password(password, employee.Password)
            
            if flag:
                request.session['employee'] = employee.id
                request.session['name'] = employee.Name
                # Name = customer.first_name
                # print("Name: ",request.session['customer'])
                return redirect('addpro')
            else:
                error_message = "Invalid Credentials"
        else:
            error_message = 'Invalid Credentials'


        return render(request, 'e_login.html', {'error': error_message})
    

def Logout(request):
    try:
        del request.session['employee']
        return redirect('e_login')
    except:
        return redirect('e_login')