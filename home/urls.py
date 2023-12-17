from django.contrib import admin
from django.urls import path
from .views import home, login, signup, description, addproject, esignup, elogin, addapplicant,sapplication, sproject, eproject


urlpatterns = [
    path('', home.Index.as_view(), name='home'),
    path('login/', login.Login.as_view(), name='s_login'),
    path('signup/', signup.Signup.as_view(), name='s_signup'),
    path('logout/', login.Logout, name='s_logout'),
    path('description/', description.Description.as_view(), name='description'),
    path('employee_login/', elogin.EmployeeLogin.as_view(), name='e_login'),
    path('employee_signup/', esignup.EmployeeSignup.as_view(), name='e_signup'),
    path('elogout/', elogin.Logout, name='e_logout'),
    path('add_project/', addproject.AddProject.as_view(), name='addpro'),
    path('apply/', addapplicant.AddApplicant.as_view(), name='apply'),
    path('application/', sapplication.StudentApplication.as_view(), name='s_application'),
    path('sproject/', sproject.StudentProject.as_view(), name='s_project'),
    path('eproject/', eproject.EmployeProject.as_view(), name='e_project'),


]