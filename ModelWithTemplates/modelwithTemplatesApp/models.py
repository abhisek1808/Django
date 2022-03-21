from django.db import models

# Create your models here.
class student(models.Model):
    School_Name=models.CharField(max_length=20)
    sname=models.CharField(max_length=20)
    sroll=models.IntegerField()
    Tenth_Board_mark=models.FloatField()
    
