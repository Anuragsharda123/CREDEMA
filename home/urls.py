from django.urls import path
from .views import e_chat, home, login, signup, description, addproject, esignup, elogin, addapplicant, sapplication, sproject, eproject, forget, otp, eforget, eotp, edescription, updatepro, applicants, studentinfo, updatestu, student_profile, emp_profile, updateemp, submitted, allocate, add_project_taskwise, update_project_taskwise, taskapplicant, taskapply, teams, s_profile, s_t_description, p_s_update, s_chat, e_chat


urlpatterns = [
    path('', home.Index.as_view(), name='home'),

    # Student Side URLs
    path('login/', login.Login.as_view(), name='s_login'),
    path('signup/', signup.Signup.as_view(), name='s_signup'),
    path('logout/', login.Logout, name='s_logout'),
    path('description/', description.Description.as_view(), name='description'),
    path('s_t_description/', s_t_description.S_T_Description.as_view(), name='s_t_description'),
    path('p_s_update/',p_s_update.P_S_Update.as_view(), name='p_s_update'),
    path('profile/', student_profile.Studentprofile.as_view(), name='s_profile'),
    path('s_profile/', s_profile.S_profile.as_view(), name='stu_profile'),
    path('editprofile', updatestu.Updatestudent.as_view(), name='update_student'),
    path('apply/', addapplicant.AddApplicant.as_view(), name='apply'),
    path('application/', sapplication.StudentApplication.as_view(), name='s_application'),
    path('task_application/', taskapplicant.AddTaskApplicant.as_view(), name='t_application'),
    path('task_apply/', taskapply.TaskApply.as_view(), name='t_apply'),
    path('teams/', teams.Teams.as_view(), name='teams'),
    path('sproject/', sproject.StudentProject.as_view(), name='s_project'),
    path('ereset/', forget.EmailReset.as_view(), name='email_reset'),
    path('sendotp/', otp.OTP.as_view(), name='send_otp'),
    path('resetpassword/', otp.ResetPassword.as_view(), name='reset_password'),

    path('student-chat/', s_chat.S_Chat.as_view(), name="s_chat"),
    

    # Employee Side URLs
    path('employee_login/', elogin.EmployeeLogin.as_view(), name='e_login'),
    path('employee_signup/', esignup.EmployeeSignup.as_view(), name='e_signup'),
    path('elogout/', elogin.Logout, name='e_logout'),
    path('edescription/', edescription.Description.as_view(), name='e_description'),
    path('emp_profile/', emp_profile.Employeeprofile.as_view(), name='e_profile'),
    path('editemploye/', updateemp.Updateemploye.as_view(), name='update_emp'),
    path('add_project/', addproject.AddProject.as_view(), name='addpro'),
    path('add_project_taskwise/', add_project_taskwise.AddProjectTask.as_view(), name='addtaskpro'),
    path('update/', updatepro.Updateproject.as_view(), name='up_pro'),
    path('update_project_taskwise/', update_project_taskwise.UpdateProjectTaskwise.as_view(), name='update_task'),
    path('eproject/', eproject.EmployeProject.as_view(), name='e_project'),
    path('e_ereset/', eforget.EmailReset.as_view(), name='e_email_reset'),
    path('e_sendotp/', eotp.OTP.as_view(), name='e_send_otp'),
    path('applicant/', applicants.Applicants.as_view(), name="applicant"),
    path('eresetpassword/', eotp.ResetPassword.as_view(), name='e_reset_password'),
    path('studentinfo/', studentinfo.Studentinfo.as_view(), name='s_info'),
    path('Submitted/', submitted.SubmittedProject.as_view(), name='c_pro'),
    path('allocate/', allocate.Allocate.as_view(), name='allocate'),
    
    path('employe-chat/', e_chat.E_Chat.as_view(), name="e_chat"),

    

]