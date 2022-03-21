from django.contrib import admin
from modelwithTemplatesApp2.models import CarsModel,BikesModel
# Register your models here.

class car(admin.ModelAdmin):
    list_display=['Car_Brand','Car_Model','Car_Price','Car_image']
admin.site.register(CarsModel,car)

class Bike(admin.ModelAdmin):
    list_display=['Bike_Brand','Bike_Model','Bike_Price']
admin.site.register(BikesModel,Bike)
