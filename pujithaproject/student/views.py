from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import CustomUser
from student.models import Student


# Create your views here.
def student_home(request):
    return render(request,'student.html')


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        qualification = request.POST.get("qualification")
        tech_stack = request.POST.get("tech_stack")
        year_of_passing = request.POST.get("year_of_passing")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('add_student')

        # Create CustomUser
        user = CustomUser.objects.create_user(
            username=email,
            first_name=name,
            email=email,
            password=password,  # Auto hashed!
            user_type="student",
            is_staff=False,
            is_active=True,
        )

        # Create Student profile
        Student.objects.create(
            user=user,
            qualification=qualification,
            tech_stack=tech_stack,
            year_of_passing=year_of_passing,
            mobile=mobile
        )

        messages.success(request, "Student added successfully!")
        return redirect('view_students')

    return render(request,'add_students.html',{'action':'Add'})





def student_profile(request):
    return HttpResponse('student profile')


def available_drives(request):
    return HttpResponse('available drives')


def applied_drives(request):
    return HttpResponse('applied drives')


def view_students(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'view_students.html',context)














def update_students(request,id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.qualification = request.POST.get('qualification')
        student.tech_stack = request.POST.get('tech_stack')
        student.year_of_passing = request.POST.get('year_of_passing')
        student.mobile = request.POST.get('mobile')
        student.save()
        return redirect('view_students')
    return render(request, 'add_students.html', {'student': student, 'action': 'update'})


def delete_students(request,id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('view_students')
