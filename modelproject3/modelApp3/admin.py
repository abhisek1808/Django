from django.contrib import admin
from modelApp3.models import Employee

# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display=['eid','ename','esal']

admin.site.register(Employee,empadmin)