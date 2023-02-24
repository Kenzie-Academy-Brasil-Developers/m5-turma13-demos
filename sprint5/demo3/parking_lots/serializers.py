from rest_framework import serializers
from .models import ParkingLot
from accounts.serializers import AccountSerializer


class ParkingLotSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)

    class Meta:
        model = ParkingLot
        fields = ["id", "name", "is_active", "account"]
        # read_only_fields = ["account"]
        # depth = 1
        # fields = "__all__"
