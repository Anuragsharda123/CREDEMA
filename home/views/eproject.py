from django.shortcuts import render,redirect
from home.models.employe import Employe
from home.models.student import Student
from home.models.project import Project
from django.core.mail import send_mail
from datetime import date, timedelta
from django.views import View
from credma import settings

class EmployeProject(View):
    def get(self, request):
        try:
            if request.session['employee']:
                emp = request.session['employee']
                employe = Employe.objects.get(id=emp)
                projects = Project.objects.filter(Employe=employe, Status='False')|Project.objects.filter(Employe=employe, Status_1=False).exclude(Student_1=None)|Project.objects.filter(Employe=employe, Status_2=False).exclude(Student_2=None)|Project.objects.filter(Employe=employe, Status_3=False).exclude(Student_3=None)|Project.objects.filter(Employe=employe, Status_4=False).exclude(Student_4=None)|Project.objects.filter(Employe=employe, Status_5=False).exclude(Student_5=None)|Project.objects.filter(Employe=employe, Status_6=False).exclude(Student_6=None)|Project.objects.filter(Employe=employe, Status_7=False).exclude(Student_7=None)|Project.objects.filter(Employe=employe, Status_8=False).exclude(Student_8=None)|Project.objects.filter(Employe=employe, Status_9=False).exclude(Student_9=None)|Project.objects.filter(Employe=employe, Status_10=False).exclude(Student_10=None)|Project.objects.filter(Employe=employe, Status_11=False).exclude(Student_11=None)|Project.objects.filter(Employe=employe, Status_12=False).exclude(Student_12=None)
                t_pro = Project.objects.filter(Status_1=False).exclude(Student_1=None)|Project.objects.filter(Status_2=False).exclude(Student_2=None)|Project.objects.filter(Status_3=False).exclude(Student_3=None)|Project.objects.filter(Status_4=False).exclude(Student_4=None)|Project.objects.filter(Status_5=False).exclude(Student_5=None)|Project.objects.filter(Status_6=False).exclude(Student_6=None)|Project.objects.filter(Status_7=False).exclude(Student_7=None)|Project.objects.filter(Status_8=False).exclude(Student_8=None)|Project.objects.filter(Status_9=False).exclude(Student_9=None)|Project.objects.filter(Status_10=False).exclude(Student_10=None)|Project.objects.filter(Status_11=False).exclude(Student_11=None)|Project.objects.filter(Status_12=False).exclude(Student_12=None)

                data = {}
                
                pro = Project.objects.all().exclude(Student=None)
                for i in pro:
                    stu = i.Student
                    student = Student.objects.get(Email=stu)

                    if(i.Status):
                        continue
                    else:
                        if student.is_Suspended:
                            if date.today()>student.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                                student.is_Suspended = False
                                student.save()
                        
                        else:
                            if date.today() == i.Duration-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                            
                            elif date.today() == i.Duration-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                                
                            elif date.today() == i.Duration-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                            
                            elif date.today() == i.Duration:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                            
                            elif date.today() > i.Duration:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student.Email])
                                student.is_Suspended = True
                                student.Suspend_till = date.today()+timedelta(days=21)
                                student.save()
                                i.Student = None
                                i.save()
                            
                            else:
                                pass


                for i in t_pro:
                    if(i.Student_1):
                        stu_1 = i.Student_1
                        student_1 = Student.objects.get(Email=stu_1)

                        if student_1.is_Suspended:
                            if date.today()>student_1.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_1.Email])
                                student_1.is_Suspended = False
                                student_1.save()
                        
                        else:
                            if date.today() == i.Duration_1-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_1.Email])
                            
                            elif date.today() == i.Duration_1-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_1.Email])
                                
                            elif date.today() == i.Duration_1-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_1.Email])
                            
                            elif date.today() == i.Duration_1:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_1.Email])
                            
                            elif date.today() > i.Duration_1:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_1.Email])
                                student_1.is_Suspended = True
                                student_1.Suspend_till = date.today()+timedelta(days=21)
                                student_1.save()
                                i.Student_1 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_2):
                        stu_2 = i.Student_2
                        student_2 = Student.objects.get(Email=stu_2)

                        if student_2.is_Suspended:
                            if date.today()>student_2.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_2.Email])
                                student_2.is_Suspended = False
                                student_2.save()
                        
                        else:
                            if date.today() == i.Duration_2-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_2.Email])
                            
                            elif date.today() == i.Duration_2-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_2.Email])
                                
                            elif date.today() == i.Duration_2-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_2.Email])
                            
                            elif date.today() == i.Duration_2:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_2.Email])
                            
                            elif date.today() > i.Duration_2:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_2.Email])
                                student_2.is_Suspended = True
                                student_2.Suspend_till = date.today()+timedelta(days=21)
                                student_2.save()
                                i.Student_2 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_3):
                        stu_3 = i.Student_3
                        student_3 = Student.objects.get(Email=stu_3)

                        if student_3.is_Suspended:
                            if date.today()>student_3.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_3.Email])
                                student_3.is_Suspended = False
                                student_3.save()
                        
                        else:
                            if date.today() == i.Duration_3-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_3.Email])
                            
                            elif date.today() == i.Duration_3-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_3.Email])
                                
                            elif date.today() == i.Duration_3-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_3.Email])
                            
                            elif date.today() == i.Duration_3:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_3.Email])
                            
                            elif date.today() > i.Duration_3:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_3.Email])
                                student_3.is_Suspended = True
                                student_3.Suspend_till = date.today()+timedelta(days=21)
                                student_3.save()
                                i.Student_3 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_4):
                        stu_4 = i.Student_4
                        student_4 = Student.objects.get(Email=stu_4)

                        if student_4.is_Suspended:
                            if date.today()>student_4.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_4.Email])
                                student_4.is_Suspended = False
                                student_4.save()
                        
                        else:
                            if date.today() == i.Duration_4-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_4.Email])
                            
                            elif date.today() == i.Duration_4-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_4.Email])
                                
                            elif date.today() == i.Duration_4-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_4.Email])
                            
                            elif date.today() == i.Duration_4:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_4.Email])
                            
                            elif date.today() > i.Duration_4:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_4.Email])
                                student_4.is_Suspended = True
                                student_4.Suspend_till = date.today()+timedelta(days=21)
                                student_4.save()
                                i.Student_4 = None
                                i.save()
                            
                            else:
                                pass

                    if(i.Student_5):
                        stu_5 = i.Student_5
                        student_5 = Student.objects.get(Email=stu_5)

                        if student_5.is_Suspended:
                            if date.today()>student_5.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_5.Email])
                                student_5.is_Suspended = False
                                student_5.save()
                        
                        else:
                            if date.today() == i.Duration_5-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_5.Email])
                            
                            elif date.today() == i.Duration_5-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_5.Email])
                                
                            elif date.today() == i.Duration_5-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_5.Email])
                            
                            elif date.today() == i.Duration_5:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_5.Email])
                            
                            elif date.today() > i.Duration_5:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_5.Email])
                                student_5.is_Suspended = True
                                student_5.Suspend_till = date.today()+timedelta(days=21)
                                student_5.save()
                                i.Student_5 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_6):
                        stu_6 = i.Student_6
                        student_6 = Student.objects.get(Email=stu_6)

                        if student_6.is_Suspended:
                            if date.today()>student_6.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_6.Email])
                                student_6.is_Suspended = False
                                student_6.save()
                        
                        else:
                            if date.today() == i.Duration_6-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_6.Email])
                            
                            elif date.today() == i.Duration_6-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_6.Email])
                                
                            elif date.today() == i.Duration_6-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_6.Email])
                            
                            elif date.today() == i.Duration_6:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_6.Email])
                            
                            elif date.today() > i.Duration_6:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_6.Email])
                                student_6.is_Suspended = True
                                student_6.Suspend_till = date.today()+timedelta(days=21)
                                student_6.save()
                                i.Student_6 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_7):
                        stu_7 = i.Student_7
                        student_7 = Student.objects.get(Email=stu_7)

                        if student_7.is_Suspended:
                            if date.today()>student_7.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_7.Email])
                                student_7.is_Suspended = False
                                student_7.save()
                        
                        else:
                            if date.today() == i.Duration_7-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_7.Email])
                            
                            elif date.today() == i.Duration_7-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_7.Email])
                                
                            elif date.today() == i.Duration_7-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_7.Email])
                            
                            elif date.today() == i.Duration_7:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_7.Email])
                            
                            elif date.today() > i.Duration_7:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_7.Email])
                                student_7.is_Suspended = True
                                student_7.Suspend_till = date.today()+timedelta(days=21)
                                student_7.save()
                                i.Student_7 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_8):
                        stu_8 = i.Student_8
                        student_8 = Student.objects.get(Email=stu_8)

                        if student_8.is_Suspended:
                            if date.today()>student_8.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_8.Email])
                                student_8.is_Suspended = False
                                student_8.save()
                        
                        else:
                            if date.today() == i.Duration_8-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_8.Email])
                            
                            elif date.today() == i.Duration_8-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_8.Email])
                                
                            elif date.today() == i.Duration_8-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_8.Email])
                            
                            elif date.today() == i.Duration_8:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_8.Email])
                            
                            elif date.today() > i.Duration_8:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_8.Email])
                                student_8.is_Suspended = True
                                student_8.Suspend_till = date.today()+timedelta(days=21)
                                student_8.save()
                                i.Student_8 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_9):
                        stu_9 = i.Student_9
                        student_9 = Student.objects.get(Email=stu_9)

                        if student_9.is_Suspended:
                            if date.today()>student_9.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_9.Email])
                                student_9.is_Suspended = False
                                student_9.save()
                        
                        else:
                            if date.today() == i.Duration_9-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_9.Email])
                            
                            elif date.today() == i.Duration_9-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_9.Email])
                                
                            elif date.today() == i.Duration_9-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_9.Email])
                            
                            elif date.today() == i.Duration_9:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_9.Email])
                            
                            elif date.today() > i.Duration_9:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_9.Email])
                                student_9.is_Suspended = True
                                student_9.Suspend_till = date.today()+timedelta(days=21)
                                student_9.save()
                                i.Student_9 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_10):
                        stu_10 = i.Student_10
                        student_10 = Student.objects.get(Email=stu_10)

                        if student_10.is_Suspended:
                            if date.today()>student_10.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_10.Email])
                                student_10.is_Suspended = False
                                student_10.save()
                        
                        else:
                            if date.today() == i.Duration_10-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_10.Email])
                            
                            elif date.today() == i.Duration_10-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_10.Email])
                                
                            elif date.today() == i.Duration_10-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_10.Email])
                            
                            elif date.today() == i.Duration_10:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_10.Email])
                            
                            elif date.today() > i.Duration_10:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_10.Email])
                                student_10.is_Suspended = True
                                student_10.Suspend_till = date.today()+timedelta(days=21)
                                student_10.save()
                                i.Student_10 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_11):
                        stu_11 = i.Student_11
                        student_11 = Student.objects.get(Email=stu_11)

                        if student_11.is_Suspended:
                            if date.today()>student_11.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_11.Email])
                                student_11.is_Suspended = False
                                student_11.save()
                        
                        else:
                            if date.today() == i.Duration_11-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_11.Email])
                            
                            elif date.today() == i.Duration_11-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_11.Email])
                                
                            elif date.today() == i.Duration_11-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_11.Email])
                            
                            elif date.today() == i.Duration_11:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_11.Email])
                            
                            elif date.today() > i.Duration_11:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_11.Email])
                                student_11.is_Suspended = True
                                student_11.Suspend_till = date.today()+timedelta(days=21)
                                student_11.save()
                                i.Student_11 = None
                                i.save()
                            
                            else:
                                pass
                                                
                    if(i.Student_12):
                        stu_12 = i.Student_12
                        student_12 = Student.objects.get(Email=stu_12)

                        if student_12.is_Suspended:
                            if date.today()>student_12.Suspend_till:
                                body = "Your Account is activate now you can apply for projects and hope now you will complete your projects before the deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_12.Email])
                                student_12.is_Suspended = False
                                student_12.save()
                        
                        else:
                            if date.today() == i.Duration_12-timedelta(days=15):
                                body = ' You have only 15 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_12.Email])
                            
                            elif date.today() == i.Duration_12-timedelta(days=7):
                                body = ' You have only 7 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be SUSPENDED for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_12.Email])
                                
                            elif date.today() == i.Duration_12-timedelta(days=1):
                                body = ' You have only 1 days left to Submit Project: ' + i.Name + ". Submit it before deadline or your account will be suspended for 20 days"
                                subject = "CREDEMA - LAST WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_12.Email])
                            
                            elif date.today() == i.Duration_12:
                                body = ' Today is the Last day to Submit Project: ' + i.Name + ". If Project isn't submitted today, then your account will be suspended for 20 days"
                                subject = "CREDEMA - WARNING"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_12.Email])
                            
                            elif date.today() > i.Duration_12:
                                body = "Your Account is Suspended for 20 daysProject as you haven't Complete the Project " + i.Name + " before deadline" 
                                subject = "CREDEMA - ACCOUNT SUSPENDED"
                                send_mail(subject, body, settings.EMAIL_HOST_USER, [student_12.Email])
                                student_12.is_Suspended = True
                                student_12.Suspend_till = date.today()+timedelta(days=21)
                                student_12.save()
                                i.Student_12 = None
                                i.save()
                            
                            else:
                                pass



                            
                data['projects'] = projects
                data['employe'] = employe

                return render(request, 'e_project.html', data)
        except:
            return redirect('e_login')