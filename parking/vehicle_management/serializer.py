from vehicle_management.models import vehicle
from rest_framework import serializers

class vehicle_serializer(serializers.ModelSerializer):
    class Meta:
        model=vehicle
        fields=['placa','marca','color_vehiculo','modelo']
        