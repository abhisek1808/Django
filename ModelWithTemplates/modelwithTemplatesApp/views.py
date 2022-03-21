from django.shortcuts import render
from modelwithTemplatesApp.models import student
# Create your views here.

def studentview(request):
    student_list=student.objects.all()
    dict={'student_list':student_list}
    return render(request,'modelwithTemplatesApp/student.html',context=dict)
