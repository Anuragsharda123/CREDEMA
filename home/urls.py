from django.contrib import admin
from django.urls import path
from .views import home, login, signup, description, addproject, esignup, elogin, addapplicant,sapplication, sproject, eproject, forget, otp, eforget, eotp, edescription, updatepro


urlpatterns = [
    path('', home.Index.as_view(), name='home'),
    path('login/', login.Login.as_view(), name='s_login'),
    path('signup/', signup.Signup.as_view(), name='s_signup'),
    path('logout/', login.Logout, name='s_logout'),
    path('description/', description.Description.as_view(), name='description'),
    path('edescription/', edescription.Description.as_view(), name='e_description'),
    path('employee_login/', elogin.EmployeeLogin.as_view(), name='e_login'),
    path('employee_signup/', esignup.EmployeeSignup.as_view(), name='e_signup'),
    path('elogout/', elogin.Logout, name='e_logout'),
    path('add_project/', addproject.AddProject.as_view(), name='addpro'),
    path('update/', updatepro.Updateproduct.as_view(), name='up_pro'),
    path('apply/', addapplicant.AddApplicant.as_view(), name='apply'),
    path('application/', sapplication.StudentApplication.as_view(), name='s_application'),
    path('sproject/', sproject.StudentProject.as_view(), name='s_project'),
    path('eproject/', eproject.EmployeProject.as_view(), name='e_project'),
    path('ereset/', forget.EmailReset.as_view(), name='email_reset'),
    path('e_ereset/', eforget.EmailReset.as_view(), name='e_email_reset'),
    path('sendotp/', otp.OTP.as_view(), name='send_otp'),
    path('e_sendotp/', eotp.OTP.as_view(), name='e_send_otp'),
    path('resetpassword/', otp.ResetPassword.as_view(), name='reset_password'),
    path('eresetpassword/', eotp.ResetPassword.as_view(), name='e_reset_password'),


]