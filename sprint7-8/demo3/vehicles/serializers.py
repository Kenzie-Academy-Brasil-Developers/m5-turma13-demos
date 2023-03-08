from rest_framework import serializers
from .models import Vehicle
from datetime import timedelta


class ReportSerializer(serializers.ModelSerializer):
    time_spend = serializers.SerializerMethodField()
    floor = serializers.SerializerMethodField()
    parking_lot = serializers.SerializerMethodField()

    def get_time_spend(self, obj: Vehicle) -> timedelta:
        # Caso não exista paid_at (None), tratar erro lógico
        return obj.arrived_at - obj.paid_at

    def get_floor(self, obj: Vehicle) -> dict:
        return {
            "floor_id": obj.spot.floor.id,
            "floor_name": obj.spot.floor.name,
        }

    def get_parking_lot(self, obj: Vehicle) -> dict:
        return {
            "parking_lot_id": obj.spot.floor.parking_lot.id,
            "parking_lot_name": obj.spot.floor.parking_lot.name,
            "owner": obj.spot.floor.parking_lot.account.username,
        }

    class Meta:
        model = Vehicle
        fields = [
            "id",
            "license_plate",
            "vehicle_type",
            "arrived_at",
            "paid_at",
            "time_spend",  # nao tem na model
            "amount_paid",
            "spot",
            "floor",  # nao tem na model
            "parking_lot",  # nao tem na model
        ]


class VehicleCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "license_plate",
            "vehicle_type",
            "arrived_at",
            "amount_paid",
            "paid_at",
            "spot",
        ]
        read_only_fields = fields


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "license_plate",
            "vehicle_type",
            "arrived_at",
            "amount_paid",
            "paid_at",
            "vehicle_image",
        ]
