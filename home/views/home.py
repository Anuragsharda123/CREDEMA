from django.shortcuts import render
from django.views import View
from home.models.project import Project

class Index(View):
    def get(self, request):
        # request.session.clear()
        try:
            del request.session['otp']
        except:
            pass
        
        search = request.GET.get('search')
        projects = Project.objects.all()
            
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
        return render(request, "project_list.html", data)
            