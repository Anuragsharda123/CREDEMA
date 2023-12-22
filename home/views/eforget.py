from django.core.mail import send_mail
from django.shortcuts import render, redirect
from home.models.employe import Employe
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
        
        return render(request, 'e_email_reset.html')
    
    def post(self, request):
        email = request.POST.get('email')
        print(email)
        error_message = None
        res = None
        
        try:
            if Employe.objects.get(Email=email):
                obj = Employe.objects.get(Email=email)
                otp = randint(100000,999999)
                request.session['otp'] = otp
                request.session['obj'] = obj.id

                body = 'Your OTP for generating new password: ' + str(otp)
                subject = "Forget Password"

                res = send_mail(subject, body, settings.EMAIL_HOST_USER, [obj.Email])
        
        except:
            error_message = "Email doesn't Exist"
            return render(request, 'e_email_reset.html',{"error":error_message})
        
        print(error_message)
        return redirect('e_send_otp')