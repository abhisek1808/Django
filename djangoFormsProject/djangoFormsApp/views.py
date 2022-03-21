from django.shortcuts import render
from djangoFormsApp.forms import studentForms
# Create your views here.
def studentView(request):
    obj=studentForms()
    dict={'form':obj}
    return render(request,'djangoFormsApp/form.html',context=dict )
