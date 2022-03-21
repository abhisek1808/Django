from django.contrib import admin
from modelApp2.models import student
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display=['sid','sname','saddr']
    
admin.site.register(student,studentadmin)