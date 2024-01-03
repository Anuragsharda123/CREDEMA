from django.shortcuts import render
from django.views import View
from home.models.student import Student
from home.models.project import Project

class Index(View):
    def get(self, request):
        student = None
        # request.session.clear()
        try:
            del request.session['otp']
        except:
            pass
        
        try:
            if request.session['student']:
                stu_id = request.session['student']
                student = Student.objects.get(id=stu_id)
        except:
            pass

        search = request.GET.get('search')
        projects = Project.objects.filter(Student=None)
            
        data = {}
        if search:
            search = search.lower()
            projects = Project.get_project_by_search(search)
                    
            # try:
            #     stu = request.session['student']
            #     stud = Student.objects.get(id=stu)
            

            # print(data)
            # except:
            #     pass
            
        data['projects'] = projects
        data['student'] = student
        return render(request, "project_list.html", data)
            