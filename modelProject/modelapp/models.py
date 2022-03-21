from django.db import models

class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=20)
    smark=models.FloatField()
    saddr=models.CharField(max_length=30)
