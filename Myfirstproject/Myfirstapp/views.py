from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):
    resp='<h1 style="color:red; text-align:center;">Hi Nani.... i Love you.....</h1>'
    return HttpResponse(resp)
