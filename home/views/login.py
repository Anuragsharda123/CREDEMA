from django.contrib.auth. hashers import check_password
from django.shortcuts import render, redirect
from home.models.student import Student
from django.views import View
from datetime import date

class Login(View):
    def get(self, request):
        try:
            if request.session['student']:
                return redirect('home')
        except:
            return render(request, "s_login.html")
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None

        try:
            student = Student.objects.get(Email=email)
        except:
            student = False

        if student:
            flag = check_password(password, student.Password)
            if flag:
                if student.is_Suspended:
                    if student.Suspend_till<date.today():
                        student.is_Suspended=False
                        student.save()
                        request.session['student'] = student.id
                        request.session['name'] = student.Name
                    
                        return redirect('home')
                    else:
                        error_message = "Your account is Suspended till " + str(student.Suspend_till) +", for not completing project on time "
                else:
                    request.session['student'] = student.id
                    request.session['name'] = student.Name
                    return redirect('home')
            else:
                error_message = "Invalid Credentials"
        else:
            error_message = "Invalid Credentials"


        return render(request, 's_login.html', {'error': error_message})
    

def Logout(request):
    try:
        del request.session['student']
        return redirect('s_login')
    except:
        return redirect('s_login')