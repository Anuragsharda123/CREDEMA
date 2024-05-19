from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from home.models.student import Student
from django.views import View


class Signup(View):
    def get(self, request):
        try:
            if request.session['student']:
                return redirect('home')
        except:
            return render(request, "s_signup.html")
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        photo = request.FILES['photo']
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        complete = request.POST.get('pass')
        university = request.POST.get('university')
        rollno = int(request.POST.get('rollno'))
        course = request.POST.get('course')
        project = request.POST.get('project')
        resume = request.FILES['resume']
        social1 = request.POST.get('social1')
        social2 = request.POST.get('social2')
        social3 = request.POST.get('social3')
        exp1 = request.POST.get('exp1')
        exp2 = request.POST.get('exp2')
        exp3 = request.POST.get('exp3')
        skills = request.POST.getlist('skill')
        sk = ""

        for i in skills:
            if(not len(sk)):
                sk = sk+i
            else:
                sk = sk + ", " + i
        
        skill = sk.lower()

        value = {
            'name': name,
            'phone': phone,
            'email': email
        }

        student = Student(Email=email, Password=password, Name=name, Age=age, University_name=university,
                          Gender=gender, Phone=phone, Country=country, State=state, City=city, 
                          Address=address, Passed=complete, Roll_no=rollno, Course=course, Projects=project, Resume=resume,
                          Social1=social1, Social2=social2, Social3=social3, Exp1=exp1, Exp2=exp2, Exp3=exp3, Skills=skill, Photo=photo)
        
        error_message = None

        if (len(name)<3):
            error_message = "Enter a valid first name!"

        if age<0:
            error_message = "Enter valid age"
        
        if (len(phone)>12 or len(phone)<7 or int(phone)<0):
            error_message = "Enter valid phone number!"
        
        isExist = Student.objects.filter(Phone=phone)
        if isExist:
            error_message = "Phone number already exists!"

        if (len(email)<11):
            error_message = "Invalid Email!"

        if (len(password)<8):
            error_message = "Password must be of 8 char!"

        if rollno<0:
            error_message = "Enter Valid Roll no."

        if (password != confirmpassword):
            error_message = "Password mismatch"
        
        # if res[-4:] != '.pdf':
        #     error_message = "Only .pdf files are accepted"

        isExist = Student.objects.filter(Email=email)
        if isExist:
            error_message = "Email already exists!"
        
        if ("@" not in email) or (email[-4:] != '.com'):
            error_message = "Enter Valid E-mail"

        if not error_message:
            student.Password = make_password(student.Password)
            student.save()
            return redirect('s_login')

        else:
            data = {
                'error': error_message,
                'values': value
            }
        return render(request,'s_signup.html', data)