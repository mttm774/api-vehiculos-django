from django.contrib import admin

from vehicle_management.models import vehicle

# Register your models here.


@admin.register(vehicle)
class vehicle_admin(admin.ModelAdmin):
    list_display=['placa','marca']