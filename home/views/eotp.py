from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from home.models.employe import Employe
from django.views import View


class OTP(View):
    def get(self, request):
        try:
            if request.session['otp']:
                return render(request, 'e_send_otp.html')
        
        except:
            try:
                if request.session['employee']:
                    return redirect('e_project')
                
            except:
                return redirect('e_project')


    def post(self, request):
        otp = int(request.POST.get('otp'))
        print(otp)
        print(request.session['otp'])
        error_message = None

        flag =  request.session['otp'] == otp
        if flag:
            del request.session['otp']
            return redirect('e_reset_password')
        else:
            error_message = "Incorrect OTP"
            return render(request, 'e_send_otp.html',{"error":error_message})
    

class ResetPassword(View):
    def get(self, request):
        try:
            if request.session['employee']:
                return redirect('e_project')
        except:
            try:
                if request.session['otp']:
                    return redirect('e_login')
            except:
                return render(request, 'e_resetpassword.html')
    
    def post(self, request):
        error_message = None
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpass')
        print(request.session['obj'])

        if len(password)<=8:
            error_message = "Password should be greater than 8 characters"
        
        if (password != confirm_password):
            error_message = "Confirm Password Mismatch"

        if error_message:
            return render(request, 'e_resetpassword.html',{"error":error_message})
        
        try:
            obj = request.session['obj']
            employ = Employe.objects.get(id=obj)
            employ.Password = make_password(password)
            employ.save()
            return redirect('e_login')
        except:
            print(error_message)
            return render(request, 'e_resetpassword.html',{"error":error_message})