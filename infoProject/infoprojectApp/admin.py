from django.contrib import admin
from infoprojectApp.models import infoTable,carsTable,bikesTable
# Register your models here.
class infoAdmin(admin.ModelAdmin):
    list_display=['info','details','urls']
admin.site.register(infoTable,infoAdmin)

class cars(admin.ModelAdmin):
    list_display=['cars','details']
admin.site.register(carsTable,cars)

class bikes(admin.ModelAdmin):
    list_display=['bikes','details']
admin.site.register(bikesTable,bikes)