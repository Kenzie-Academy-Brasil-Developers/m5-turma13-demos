from django.db import models
from floors.models import SpotType
from django.utils import timezone

"""
    loss of significance

    1 REAL -> 100 centavos
"""


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=50, choices=SpotType.choices)
    # arrived_at = models.DateTimeField(auto_now_add=True)
    arrived_at = models.DateTimeField(default=timezone.now)
    amount_paid = models.IntegerField(null=True, default=None)
    paid_at = models.DateTimeField(null=True, default=None)
    vehicle_image = models.ImageField(null=True)

    spot = models.ForeignKey(
        "floors.Spot",
        on_delete=models.CASCADE,
        related_name="vehicles",
        null=True,
    )
