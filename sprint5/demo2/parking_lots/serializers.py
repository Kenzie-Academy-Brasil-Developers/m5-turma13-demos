from rest_framework import serializers
from .models import ParkingLot

"""
    ModelSerializer:
        - Já vem com .create e .update nativos (sua versão mais generica)
            - model.objects.create(**validated_data)
"""


class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        fields = ["id", "name"]
        # fields = "__all__"
