from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# to add and save data
def Add_Show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data["name"]
            lm = fm.cleaned_data["lastname"]
            em = fm.cleaned_data["email"]
            pw = fm.cleaned_data["password"]
            reg=User(name=nm,lastname=lm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm=StudentRegistration()

#stud is used to showcase data on the page of filling form.
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html',{"form":fm,"stu":stud})



#for update and edit the form
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request,'enroll/updatestudent.html',{"form":fm})






# to delete data
def delete_data(request,id):
    if request.method=='POST':
        data=User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')
