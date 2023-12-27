from django.shortcuts import render, redirect
from home.models.employe import Employe
from home.models.company import Company
from django.views import View


class Updateemploye(View):
    def get(self, request):
        try:
            if request.session['employee']:
                emp_id = request.session['employee']
                employe = Employe.objects.get(id=emp_id)
                companies = Company.objects.all()
                data = {}

                data['employe'] = employe
                data['companies'] = companies
                return render(request, 'empupdate.html', data)
        except: 
            return redirect('e_login')
        
    def post(self, request):
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        comp = request.POST.get('company')
        empid = int(request.POST.get('empno'))
        role = request.POST.get('role')
        social1 = request.POST.get('social1')
        social2 = request.POST.get('social2')
        social3 = request.POST.get('social3')
        error_message = None

        emp_id = request.session['employee']
        employe = Employe.objects.get(id=emp_id)
        

        if (len(name)<3):
            error_message = "Enter a valid first name!"

        if age<0:
            error_message = "Enter valid age"
        
        if (len(phone)>12 or len(phone)<7 or int(phone)<0):
            error_message = "Enter valid phone number!"
        
        isExist = Employe.objects.filter(Phone=phone).exclude(id = emp_id)
        if isExist:
            error_message = "Phone number already exists!"

        if empid<0:
            error_message = "Enter Valid Roll no."
        
        if request.POST.get('company'):
            company = Company.objects.get(id=int(comp))
            employe.Company_name = company
        


        if not error_message:
            employe.Employee_Id_no = empid
            employe.Address = address
            employe.State = state
            employe.Phone = phone
            employe.Name = name
            employe.City = city
            employe.Role = role
            employe.Age = age
            
            if request.POST.get('gender'):
                employe.Gender = gender


            if request.POST.get('country'):
                employe.Country = country

            if request.POST.get('social1'):
                employe.Social1 = social1

            if request.POST.get('social2'):
                employe.Social2 = social2

            if request.POST.get('social3'):
                employe.Social3 = social3
            
                
            employe.save()
            return redirect('e_profile')

        else:
            data = {
                'error': error_message,
                'student': employe
            }
        return render(request, 'empupdate.html', data)