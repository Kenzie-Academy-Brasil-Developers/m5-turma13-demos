from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "license_plate",
            "vehicle_type",
            "arrived_at",
            "amound_paid",
            "paid_at",
            "spot",
        ]
