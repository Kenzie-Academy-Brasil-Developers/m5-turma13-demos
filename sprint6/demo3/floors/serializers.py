from rest_framework import serializers
from .models import Floor, Spot, SpotType


class FloorSerializer(serializers.ModelSerializer):
    motorcycle_spots = serializers.IntegerField(write_only=True)
    car_spots = serializers.IntegerField(write_only=True)
    spots_count = serializers.SerializerMethodField()

    def get_spots_count(self, obj: Floor) -> dict:
        car_spots_count = obj.spots.filter(variety=SpotType.CAR).count()
        motorcycle_spots_count = obj.spots.filter(variety=SpotType.MOTORCYCLE).count()

        available_car_spots = obj.spots.filter(
            variety=SpotType.CAR, is_free=True
        ).count()
        available_motorcycle_spots = obj.spots.filter(
            variety=SpotType.MOTORCYCLE, is_free=True
        ).count()

        return {
            "car_spots": car_spots_count,
            "motorcycle_spots": motorcycle_spots_count,
            "available_car_spots": available_car_spots,
            "available_motorcycle_spots": available_motorcycle_spots,
        }

    class Meta:
        model = Floor
        fields = [
            "id",
            "name",
            "spot_priority",
            "motorcycle_spots",
            "car_spots",
            "spots_count",
            "parking_lot",
        ]
        read_only_fields = ["parking_lot"]

    def create(self, validated_data):
        car_spots_qnt = validated_data.pop("car_spots")
        motorcycle_spots_qnt = validated_data.pop("motorcycle_spots")

        # 1. Criar o piso antes para criar as vagas associadas a ele depois
        floor_obj = Floor.objects.create(**validated_data)

        # 2. Criar as vagas de carro associando com o piso
        # for _ in range(car_spots_qnt):
        #     Spot.objects.create(variety=SpotType.CAR, floor=floor_obj)

        # # 3. Criar as vagas de moto associando com o piso
        # for _ in range(motorcycle_spots_qnt):
        #     Spot.objects.create(variety=SpotType.MOTORCYCLE, floor=floor_obj)

        car_objects = [
            Spot(variety=SpotType.CAR, floor=floor_obj) for _ in range(car_spots_qnt)
        ]

        motorcycle_objects = [
            Spot(variety=SpotType.MOTORCYCLE, floor=floor_obj)
            for _ in range(motorcycle_spots_qnt)
        ]

        # Spot.objects.bulk_create(car_objects)
        # Spot.objects.bulk_create(motorcycle_objects)
        Spot.objects.bulk_create(car_objects + motorcycle_objects)

        return floor_obj


"""
for _ in range(car_spots_qnt):
            Spot.objects.create(variety=SpotType.CAR, floor=floor_obj)

# 10.000 inserts
INSERT INTO floors_spot (variety, floor_id) VALUES ('car', 1)
INSERT INTO floors_spot (variety, floor_id) VALUES ('car', 1)
INSERT INTO floors_spot (variety, floor_id) VALUES ('car', 1)
INSERT INTO floors_spot (variety, floor_id) VALUES ('car', 1)

-- BULK_CREATE 1 INSERT
INSERT INTO
	floors_spot (variety, floor_id)
VALUES
	('car', 1),
	('car', 1),
	('car', 1),
	('car', 1),
	('car', 1),
	('car', 1),
	('car', 1),
	('car', 1);
"""
