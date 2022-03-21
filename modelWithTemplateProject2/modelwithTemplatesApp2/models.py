from platform import mac_ver
from sys import maxsize
from django.db import models

# Create your models here.
class CarsModel(models.Model):
    Car_Brand=models.CharField(max_length=20)
    Car_Model=models.CharField(max_length=20)
    Car_Price=models.FloatField()
    Car_image=models.ImageField()

class BikesModel(models.Model):
    Bike_Brand=models.CharField(max_length=20)
    Bike_Model=models.CharField(max_length=20)
    Bike_Price=models.FloatField()
    
