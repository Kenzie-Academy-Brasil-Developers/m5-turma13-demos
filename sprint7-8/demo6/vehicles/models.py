from django.db import models
from django.utils import timezone
from django.utils import timezone
from datetime import timedelta
from .exceptions import CheckoutError


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10)
    color = models.CharField(max_length=100, default=None)
    arrived_at = models.DateTimeField(default=timezone.now)
    amount_paid = models.IntegerField(null=True, default=None)
    paid_at = models.DateTimeField(null=True, default=None)

    def calculate_time_spend(self) -> timedelta:
        if self.paid_at is None:
            time_interval = timezone.now() - self.arrived_at
        else:
            time_interval = self.paid_at - self.arrived_at

        return time_interval

    def calculate_amount_to_pay(self) -> float:
        time_spend = self.calculate_time_spend()
        price_per_second = 10  # R$ 0,10 por segundo
        total_to_pay = time_spend.total_seconds() * price_per_second

        return total_to_pay

    def checkout_vehicle(self):
        if self.paid_at is not None:
            raise CheckoutError

        self.paid_at = timezone.now()
        self.amount_paid = self.calculate_amount_to_pay()
        self.save()
