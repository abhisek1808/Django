from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def thirdviews(request):
    return HttpResponse('<h1><u>This is From ThirdApp</u></h1>')