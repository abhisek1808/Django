from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def amazon(request):
    dict={'heading':'_Amazon_',
    'URL':'https://www.amazon.in/'}
    return render(request,'ProductApp/display.html',context=dict)
def flipkart(request):
    dict={'heading':'_Flipkart_',
    'URL':'https://www.flipkart.com/'}
    return render(request,'ProductApp/display.html',context=dict)
def myntra(request):
    dict={'heading':'_Myntra_',
    'URL':'https://www.myntra.com/'}
    return render(request,'ProductApp/display.html',context=dict)

def index(request):
    return render(request,'ProductApp/index.html')