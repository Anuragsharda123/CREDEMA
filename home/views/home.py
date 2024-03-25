from django.shortcuts import render, redirect
from home.models.student import Student
from home.models.project import Project
from django.views import View


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
                if student.is_Suspended:
                    return redirect('s_logout')
                else:
                    pass
                        
        except:
            pass

        search = request.GET.get('search')
        projects = Project.objects.filter(Student=None)
            
        data = {}
        if search:
            search = search.lower()
            projects = Project.get_project_by_search(search)
                    
            
        data['projects'] = projects
        data['student'] = student
        return render(request, "index.html", data)
            