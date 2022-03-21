from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstviews(request):
    return HttpResponse('<h1><u>This is From FirstApp</u></h1>')