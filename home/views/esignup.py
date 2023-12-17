from django.contrib.auth.hashers import make_password
from home.models.company import Company
from home.models.employe import Employe
from django.shortcuts import render, redirect
from django.views import View

class EmployeeSignup(View):
    def get(self, request):
        try:
            if request.session['employee']:
                return redirect('e_project')
            
        except:
            data = {}
            companies = Company.objects.all()
            data['companies'] = companies

            return render(request, "e_signup.html", data)
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        comp = int(request.POST.get('company'))
        empno = int(request.POST.get('empno'))
        role = request.POST.get('role')
        social1 = request.POST.get('social1')
        social2 = request.POST.get('social2')
        social3 = request.POST.get('social3')
        error_message = None


        value = {
            'name': name,
            'phone': phone,
            'email': email
            }
        company = Company.objects.get(id=comp)
        print(company)

        employee = Employe(Email=email, Password=password, Name=name, Age=age, 
                          Gender=gender, Phone=phone, Country=country, State=state, City=city, 
                          Address=address, Social1=social1, Company_name=company, Employee_Id_no=empno,
                          Role=role, Social2=social2, Social3=social3,)
        
        if (len(name)<3):
            error_message = "Enter a valid first name!"

        if age<0:
            error_message = "Enter valid age"
        
        if (len(phone)>12 or len(phone)<7 or int(phone)<0):
            error_message = "Enter valid phone number!"
        
        isExist = Employe.objects.filter(Phone=phone)
        if isExist:
            error_message = "Phone number already exists!"

        if (len(email)<11):
            error_message = "Invalid Email!"

        if (len(password)<8):
            error_message = "Password must be of 8 char!"

        if empno<0:
            error_message = "Enter Valid Roll no."

        if (password != confirmpassword):
            error_message = "Password mismatch"

        isExist = Employe.objects.filter(Email=email)
        if isExist:
            error_message = "Email already exists!"
        
        if ("@" not in email) or (email[-4:] != '.com'):
            error_message = "Invalid Email"

        if not error_message:
            employee.Password = make_password(employee.Password)
            employee.save()
            return redirect('e_login')

        else:
            data = {
                'error': error_message,
                'values': value
            }

        return render(request, "e_signup.html", data)