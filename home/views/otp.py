from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from home.models.student import Student
from django.views import View


class OTP(View):
    def get(self, request):
        return render(request, 'send_otp.html')
    
    def post(self, request):
        otp = int(request.POST.get('otp'))
        print(otp)
        print(request.session['otp'])
        error_message = None

        flag =  request.session['otp'] == otp
        if flag:
            return redirect('reset_password')
        else:
            error_message = "Incorrect OTP"
            return render(request, 'send_otp.html',{"error":error_message})
    

class ResetPassword(View):
    def get(self, request):
        return render(request, 'resetpassword.html')
    
    def post(self, request):
        error_message = None
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpass')

        if len(password)<=8:
            error_message = "Password should be greater than 8 characters"
        
        if (password != confirm_password):
            error_message = "Confirm Password Mismatch"

        if error_message:
            return render(request, 'resetpassword.html',{"error":error_message})
        
        try:
            obj = request.session['obj']
            student = Student.objects.get(id=obj)
            student.Password = make_password(password)
            student.save()
            return redirect('s_login')
        except:
            print(error_message)
            return render(request, 'resetpassword.html',{"error":error_message})