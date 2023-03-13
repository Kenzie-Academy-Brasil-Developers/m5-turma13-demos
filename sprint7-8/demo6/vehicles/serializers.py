from rest_framework import serializers

from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "license_plate",
            "color",
            "arrived_at",
            "amount_paid",
            "paid_at",
        ]
        read_only_fields = [
            "amount_paid",
            "paid_at",
            "arrived_at",
        ]


class VehicleCheckoutSerializer(serializers.ModelSerializer):
    time_spend = serializers.CharField(source="calculate_time_spend", read_only=True)

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "license_plate",
            "color",
            "arrived_at",
            "amount_paid",
            "time_spend",
            "paid_at",
        ]
        read_only_fields = [
            "license_plate",
            "color",
            "amount_paid",
            "paid_at",
            "arrived_at",
        ]
        # read_only_fields = fields
