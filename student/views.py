from django.shortcuts import redirect, render
from .models import *
from authentication.models import customUser
from django.contrib import messages
# Create your views here.
def addStudent(request):
    error_messages = {
        'success': 'Student Add Successfully',
        'error': 'Student Add Failed',
    }
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")  # Changed from 'user_name' to 'username'
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        course_id = request.POST.get("courseid")
        session_year_id = request.POST.get("sessionyearid")

        # Check if email or username already exists
        if customUser.objects.filter(email=email).exists() or customUser.objects.filter(username=username).exists():
            messages.error(request, error_messages['error'])
        else:
            # Create the customUser instance
            user = customUser.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.profile_pic = profile_pic
            user.user_type = 3  # Assuming '3' represents students

            # Save the user instance
            user.save()

            # Retrieve the selected course and session year
            myCourse = courseModel.objects.get(id=course_id)
            mySessionYear = sessionYearModel.objects.get(id=session_year_id)

            # Create the student instance
            student = studentModel(
                admin=user,
                address=address,
                sessionyearid=mySessionYear,
                courseid=myCourse,
                gender=gender,
            )

            # Save the student instance
            student.save()

            messages.success(request, error_messages['success'])
            return redirect("studentList")

    # Fetch the course and session year data to display in the form
    course = courseModel.objects.all()
    session_year = sessionYearModel.objects.all()
    context = {
        "course": course,
        "session": session_year, 
    }

    return render(request, "Students/addStudent.html", context)



def studentList(request):
    allStudent=studentModel.objects.all()
    return render(request,"Students/studentList.html",{"student":allStudent})


def editStudent(request,id):
    student=studentModel.objects.filter(id=id)
    course = courseModel.objects.all()
    session_year = sessionYearModel.objects.all()
    st=studentModel.objects.all()
    context = {
        "course": course,
        "session": session_year,
        "student":student,
        
    }
    
    return render(request,"Students/editStudent.html",context)




def updateStudent(request):
    error_messages = {
        'success': 'Student Updated Successfully',
        'error': 'Student Updated Failed',
    }
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        student_id = request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")  # Changed from 'user_name' to 'username'
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        course_id = request.POST.get("courseid")
        session_year_id = request.POST.get("sessionyearid")
        
        user=customUser.objects.get(id=student_id)
        
        user.first_name = first_name
        user.last_name = last_name
        user.email=email
        user.username=username
        
        if password is not None and password!="":
            user.set_password(password)
        if password is not None and profile_pic!="":
            user.profile_pic=profile_pic
        user.save()
        
        student=studentModel.objects.get(admin=student_id)
        student.address=address
        student.gender=gender
        
        course=courseModel.objects.get(id=course_id)
        student.course_id=course
        
        session=sessionYearModel.objects.get(id=session_year_id)
        student.session_year_id=session
        
        student.save()
        
        
        messages.success(request, error_messages['success'])
        return redirect("studentList")
    
    return render(request,"editStudent.html")



def studentDelete(request, id):
    stu=studentModel.objects.filter(id=id)
    stu.delete()
    return redirect("studentList")