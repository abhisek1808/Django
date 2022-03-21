from os import name
from django.shortcuts import render
import datetime
# Create your views here.
def displayWish(request):
    data=datetime.datetime.now().hour
    s='<h1>Hi : '

    if data<12:
        s=s+'Good Morning'
    elif data<17:
        s=s+'God Afternoon'
    elif data<21:
        s=s+'Good Evening'
    else:
        s=s+'Good Night'
 
    s=s+'</h1>'
    dict={'s':name,'Time':data}

    return render(request,'dynamicprojectApp/dynamic.html',dict)