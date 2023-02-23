from django.db import models


class ParkingLot(models.Model):
    name = models.CharField(max_length=255)
