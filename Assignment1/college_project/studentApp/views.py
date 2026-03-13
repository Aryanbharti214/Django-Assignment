from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Student

# Create your views here.


#Q3
def student_list(request):

    students = Student.objects.all()

    return render(request, 'studentApp/student_list.html', {
        'students': students
    })


#Q4
def student_detail(request, pk):

    student = get_object_or_404(Student, pk=pk)

    return render(request, 'studentApp/student_detail.html', {
        'student': student
    })