from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Display(resqest):
    i='<h1>This is my second <span style="color: green">Django project</span></h1>'
    return HttpResponse(i)
def secondDisplay(resqest):
    j='<h1>This is my second <span style="color: green">view</span></h1>'
    return HttpResponse(j)
def thirdDisplay(resqest):
    k='<h1>This is my third <span style="color: green">view</span></h1>'
    return HttpResponse(k)