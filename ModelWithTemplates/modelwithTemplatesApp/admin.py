from django.contrib import admin
from modelwithTemplatesApp.models import student
# Register your models here.
class studentEligible(admin.ModelAdmin):
    list_display=['School_Name','sname','sroll','Tenth_Board_mark']
    
admin.site.register(student,studentEligible)
