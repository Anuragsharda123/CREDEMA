from django.shortcuts import render, redirect
from home.models.student import Student
from django.views import View


class Updatestudent(View):
    def get(self, request):
        try:
            if request.session['student']:
                stu_id = request.session['student']
                student = Student.objects.get(id=stu_id)
                data = {}

                data['student'] = student

                return render(request, 'updatestu.html', data)
        except:
            return redirect('s_login')
        
    def post(self, request):
        error_message = None
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        photo = request.POST.get('photo')
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
        resume = request.POST.get('resume')
        social1 = request.POST.get('social1')
        social2 = request.POST.get('social2')
        social3 = request.POST.get('social3')
        skills = request.POST.getlist('skill')

        for i in range(0, len(skills)):
            skills[i] = skills[i].lower()

        stu_id = request.session['student']
        student = Student.objects.get(id=stu_id)

        sk = student.Skills
        
        b = sk.split(", ")
        print(b)
        for i in b:
            if(i in skills):
                skills.remove(i)

        for i in skills:
            sk = sk + ", " +i
            
        sk = sk.lower()

        if (len(name)<3):
            error_message = "Enter a valid first name!"

        if age<0:
            error_message = "Enter valid age"
        
        if (len(phone)>12 or len(phone)<7 or int(phone)<0):
            error_message = "Enter valid phone number!"
        
        isExist = Student.objects.filter(Phone=phone).exclude(id = stu_id)
        if isExist:
            error_message = "Phone number already exists!"

        if rollno<0:
            error_message = "Enter Valid Roll no."
        
        if request.POST.get('resume'):
            if resume[-4:] != '.pdf':
                error_message = "Only .pdf files are accepted"
            else:
                student.Resume = resume


        if not error_message:
            student.Name = name
            student.Age = age
            student.Phone = phone
            student.State = state
            student.City = city
            student.Address = address
            student.University_name = university
            student.Course = course
            student.Roll_no = rollno
            student.Skills = sk
            
            if request.POST.get('photo'):
                student.Photo = photo
            
            if request.POST.get('gender'):
                student.Gender = gender
            
            if request.POST.get('pass'):
                student.Passed = complete

            if request.POST.get('country'):
                student.Country = country

            if request.POST.get('social1'):
                student.Social1 = social1

            if request.POST.get('social2'):
                student.Social2 = social2

            if request.POST.get('social3'):
                student.Social3 = social3
            
                
            student.save()
            return redirect('s_profile')

        else:
            data = {
                'error': error_message,
                'student':student
            }
        return render(request, 'updatestu.html', data)