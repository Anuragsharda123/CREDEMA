from django.shortcuts import render, redirect
from home.models.project import Project
from home.models.employe import Employe
from home.models.company import Company
from home.models.student import Student
from home.models.chat import Chat
from django.views import View

class E_Chat(View):
    def get(self, request):
        return redirect("e_project")
    
    def post(self, request):
        return redirect("e_project")
        # return render(request, "chat.html")