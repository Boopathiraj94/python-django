from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Students
# Create your views here.

def registrations(request):

    if request.method == "POST":
        name = request.POST.get('studentName')
        phone = request.POST.get('phone')
        className = request.POST.get('className')
        section = request.POST.get('section')
        email = request.POST.get('email')
        address = request.POST.get('address')
        issave = Students.objects.create(student_name=name,student_phone=phone,student_class=className,student_section=section,student_email=email,student_address=address)
        issave.save()
        all_students = Students.objects.all()
        return render(request,'register.html', {'all_students':all_students})


    all_students = Students.objects.all()
    if all_students:
        return render(request,'register.html', {'all_students':all_students})
    else:
        return render(request,'register.html')

def register(request):
    return render(request,'register.html')    

def delete_student(request,sid):
    stud = Students.objects.get(id=sid)
    stud.delete()
    return redirect('registrations')

def update_form(request,stuid):
    stud = Students.objects.get(id=stuid)
    if request.method == "POST":
        stud.student_name = request.POST.get('studentName')
        stud.student_phone = request.POST.get('phone')
        stud.student_class = request.POST.get('className')
        stud.student_section = request.POST.get('section')
        stud.student_email = request.POST.get('email')
        stud.student_address = request.POST.get('address')
        stud.save()
        return redirect("registrations")
    return render(request,'update.html',{'student': stud} )



