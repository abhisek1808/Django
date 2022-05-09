from math import fabs
from django.shortcuts import render
from captureFormApp.forms import studentform
# Create your views here.
def studentView(request):
    #creat form class object
    form=studentform() #empty form object
    #little bit validate
    name=""
    age=0
    email=""
    addr=""
    check=False
    if request.method == 'POST':
        form=studentform(request.POST) #form with data
        if form.is_valid():
            name=form.cleaned_data['sname']
            age=form.cleaned_data['sage']
            email=form.cleaned_data['semail']
            addr=form.cleaned_data['saddr']
            check=True
    return render(request,'captureFormApp/index.html',{'form':form,'name':name,'age':age,'email':email,'addr':addr,'check':check})