from django.shortcuts import redirect, render
from home.models.student import Student
from django.views import View

class Studentinfo(View):
    def get(self, request):
        return redirect('e_project')

    def post(self,request):
        stu_id = request.POST.get('stu_id')
        data = {}

        student = Student.objects.get(id=stu_id)

        data['student'] = student

        return render(request, 's_info.html', data)