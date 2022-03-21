from django.db import models

# Create your models here.
class infoTable(models.Model):
    info=models.CharField(max_length=20)
    details=models.CharField(max_length=300)
    urls=models.CharField(max_length=100)

class carsTable(models.Model):
    cars=models.CharField(max_length=20)
    details=models.CharField(max_length=300)
    
class bikesTable(models.Model):
    bikes=models.CharField(max_length=20)
    details=models.CharField(max_length=300)