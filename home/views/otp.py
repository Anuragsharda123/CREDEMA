from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from home.models.student import Student
from django.views import View


class OTP(View):
    def get(self, request):
        try:
            if request.session['otp']:
                return render(request, 'send_otp.html')
        
        except:
            try:
                if request.session['student']:
                    return redirect('home')
                
            except:
                return redirect('home')
    
    def post(self, request):
        otp = int(request.POST.get('otp'))
        print(otp)
        print(request.session['otp'])
        error_message = None

        flag =  request.session['otp'] == otp
        request.session['flag'] = flag
        if flag:
            del request.session['otp']
            return redirect('reset_password')
        else:
            error_message = "Incorrect OTP"
            return render(request, 'send_otp.html',{"error":error_message})
    

class ResetPassword(View):
    def get(self, request):
        try:
            if request.session['student']:
                return redirect('home')
        except:
            try:
                if request.session['otp']:
                    return redirect('home')
            except:
                try:
                    if request.session['flag']:
                        request.session['flag'] = 0
                        return render(request, 'resetpassword.html')
                except:
                    return redirect('home')
                
                

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
            obj = request.session['sobj']
            student = Student.objects.get(id=obj)
            student.Password = make_password(password)
            student.save()
            del request.session['sobj']
            return redirect('s_login')
        except:
            print(error_message)
            return render(request, 'resetpassword.html',{"error":error_message})