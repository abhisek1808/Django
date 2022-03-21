from django.shortcuts import render
from modelwithTemplatesApp2.models import CarsModel,BikesModel
# Create your views here.
def display(request):
    car_list=CarsModel.objects.all()
    bike_list=BikesModel.objects.all()
    dict={'car':car_list,'bike':bike_list}
    return render(request,'modelwithTemplatesApp2/views.html',context=dict)