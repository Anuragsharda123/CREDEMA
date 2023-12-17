from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect
from home.models.employe import Employe
from home.models.student import Student
from django.views import View
from credma import settings
from random import randint
    

class EmailReset(View):
    def get(self,request):
        # try:
            # if request.session['otp']:
                # return redirect('home')
        # except:
        #     try:
        #         if (request.session['student']) or (request.session['employee']):
        #             return redirect('home')
        #     except:
        #         pass
        
        return render(request, 'email_reset.html')
    
    def post(self, request):
        email = request.POST.get('email')
        print(email)
        error_message = None
        res = None
        try:
            if Student.objects.get(Email=email):
                obj = Student.objects.get(Email=email)
                otp = randint(100000,999999)
                request.session['otp'] = otp
                request.session['stu_obj'] = obj.id
                
                body = 'Your OTP for generating new password: ' + otp
                subject = "Forget Password"

                res = send_mail(subject, body, settings.EMAIL_HOST_USER, [obj.Email])
                
        except:
            # try:
            #     if Employe.objects.get(Email=email):
            #         obj = Employe.objects.get(Email=email)
            #         otp = randint(100000,999999)
            #         request.session['otp'] = otp
            #         request.session['emp_obj'] = obj.id

            #         body = 'Your OTP for generating new password: ' + otp
            #         subject = "Forget Password"

            #         res = send_mail(subject, body, settings.EMAIL_HOST_USER, [obj.Email])
            # except:
            error_message = "Email doesn't Exist"
            print(error_message)
            print(obj.Email)
            print(res)
            return render(request, 'email_reset.html',{"error":error_message})
        print(error_message)
        return redirect('send_otp')
        

class OTP(View):
    def get(self, request):
        return render(request, 'send_otp.html')
    
    def post(self, request):
        otp = request.POST.get('otp')
        error_message = None

        flag =  request.session['otp'] == otp
        if flag:
            return redirect('reset_password')
        else:
            error_message = "Incorrect OTP"
            return render(request, 'send_otp.html',{"error":error_message})
    

class ResetPassword(View):
    def get(self, request):
        request.session['otp'].clear()
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
            obj = request.session['stu_obj']
            student = Student.objects.get(id=obj)
            student.Password = make_password(password)
            student.save()
            return redirect('home')
        except:
            return render(request, 'resetpassword.html',{"error":error_message})

        