from django.shortcuts import render
from infoprojectApp.models import infoTable,carsTable,bikesTable
# Create your views here.

def display(request):
    info_list=infoTable.objects.all()
    dict={'info_list':info_list}
    return render(request,'infoprojectApp/index.html',context=dict)

def display2(request):
    info_list=carsTable.objects.all()
    dict={'info_list2':info_list}
    return render(request,'infoprojectApp/display.html',context=dict)

def display3(request):
    info_list=bikesTable.objects.all()
    dict={'info_list3':info_list}
    return render(request,'infoprojectApp/display.html',context=dict)

