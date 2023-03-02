from django.core.management import base
from typing import Any, Optional
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserType
from parking_lots.models import ParkingLot
from floors.models import Floor, Spot, SpotType
from vehicles.models import Vehicle
import random
from faker import Faker
from django.utils import timezone
from datetime import datetime, timedelta

fake = Faker("pt_BR")

# from accounts.models import Account

User: UserType = get_user_model()


class Command(base.BaseCommand):
    help = "Ajuda para o comando"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        """
        1. Criar contas, estacionamentos, pisos, vagas e veiculos
        """
        self.stdout.write(self.style.WARNING("seeding data...\n"))
        admin_data = {
            "username": "lucira",
            "email": "lucirodonte@mail.com",
            "first_name": "Lu",
            "last_name": "Cira",
            "password": "1234",
            "is_superuser": True,
        }

        user1_data = {
            "username": "alexandre",
            "first_name": "Ale",
            "last_name": "Xandre",
            "email": "alenossauro@mail.com",
            "password": "1234",
        }

        # Criação de usuários
        self.stdout.write(self.style.WARNING("creating users..."))
        users_data = [admin_data, user1_data]
        users_list = [User.objects.create_user(**user_data) for user_data in users_data]
        self.stdout.write(
            self.style.SUCCESS(f"Done! [{len(users_list)} users created.]\n")
        )

        # Criação de estacionamentos
        self.stdout.write(self.style.WARNING("creating parking lots..."))
        parking_lots_names = [
            "Estacionamento Hot Wheels Parque dos Tubarões",
            "Estacionamento Hotwheels Ilha dos Astros",
        ]
        parking_lots_list = [
            ParkingLot(name=pl_name, account=random.choice(users_list))
            for pl_name in parking_lots_names
        ]
        parking_lots_bulk = ParkingLot.objects.bulk_create(parking_lots_list)
        self.stdout.write(
            self.style.SUCCESS(
                f"Done! [{len(parking_lots_bulk)} parking lots created.]\n"
            )
        )

        # Criação de pisos
        self.stdout.write(self.style.WARNING("creating floors..."))
        rand_floor_max_range = random.randint(10, 20)
        floors_list = [
            Floor(**generate_floor_info(parking_lots_bulk))
            for _ in range(4, rand_floor_max_range)
        ]
        floors_bulk = Floor.objects.bulk_create(floors_list)
        self.stdout.write(
            self.style.SUCCESS(f"Done! [{len(floors_bulk)} floors created.]\n")
        )

        # Criação das vagas
        self.stdout.write(self.style.WARNING("creating spots..."))
        spots_list = generate_spots_info(floors_bulk)
        spots_bulk = Spot.objects.bulk_create(spots_list)
        self.stdout.write(
            self.style.SUCCESS(f"Done! [{len(spots_bulk)} spots created.]\n")
        )

        # Criação de veículos
        self.stdout.write(self.style.WARNING("creating vehicles..."))
        vehicles_list = [Vehicle(**generate_vehicle_info(spot)) for spot in spots_bulk]
        vehicle_bulk = Vehicle.objects.bulk_create(vehicles_list)
        self.stdout.write(
            self.style.SUCCESS(f"Done! [{len(vehicle_bulk)} vehicles created.]\n")
        )

        self.stdout.write(self.style.SUCCESS(f"Seeding process complete!"))


def generate_vehicle_info(spot: Spot) -> dict:
    start_date = timezone.now() - timedelta(days=365)
    end_date = timezone.now() - timedelta(days=1)

    fake_arrived_at = fake.date_time_between(
        start_date=start_date, end_date=end_date, tzinfo=timezone.utc
    )
    fake_paid_at = fake_arrived_at + timedelta(
        hours=random.randint(1, 10),
        minutes=random.randint(1, 60),
        seconds=random.randint(1, 60),
    )

    time_interval: timedelta = fake_paid_at - fake_arrived_at
    total_seconds = time_interval.total_seconds()
    fake_amount_paid = total_seconds * 5

    fake_license_plate = fake.license_plate()

    vehicle_data = {
        "license_plate": fake_license_plate,
        "arrived_at": fake_arrived_at,
        "paid_at": fake_paid_at,
        "amount_paid": fake_amount_paid,
        "spot": spot,
        "vehicle_type": spot.variety,
    }

    return vehicle_data


def generate_spots_info(floors_bulk: list[Floor]) -> list[Spot]:
    spot_type_choices = [choice[0] for choice in SpotType.choices]

    spots_list = []
    for floor in floors_bulk:
        rand_range = random.randint(5, 15)

        created_spots = [
            Spot(variety=random.choice(spot_type_choices), floor=floor)
            for _ in range(1, rand_range)
        ]

        spots_list += created_spots

    return spots_list


def generate_floor_info(pl_bulk: list[ParkingLot]) -> dict:
    random_pl = random.choice(pl_bulk)
    random_spot_priority = random.randint(1, 4)
    pl_floor_count = random_pl.floors.count()

    floor_data = {
        "name": f"Floor {pl_floor_count + 1} - Parking Lot {random_pl.pk}",
        "spot_priority": random_spot_priority,
        "parking_lot": random_pl,
    }

    return floor_data
