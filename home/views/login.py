from django.contrib.auth. hashers import check_password
from django.shortcuts import render, redirect
from home.models.student import Student
from django.views import View

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

        try:
            student = Student.objects.get(Email=email)
        except:
            student = False

        error_message = None

        if student:
            flag = check_password(password, student.Password)
            
            if flag:
                request.session['student'] = student.id
                request.session['name'] = student.Name
                # Name = customer.first_name
                # print("Name: ",request.session['customer'])
                return redirect('home')
            else:
                error_message = "Invalid Credentials"
        else:
            error_message = 'Invalid Credentials'


        return render(request, 's_login.html', {'error': error_message})
    

def Logout(request):
    try:
        del request.session['student']
        return redirect('s_login')
    except:
        return redirect('s_login')