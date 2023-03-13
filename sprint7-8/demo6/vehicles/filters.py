from .models import Vehicle
from django_filters import rest_framework as filters


class VehicleFilter(filters.FilterSet):
    arrived_at_gte = filters.DateFilter(field_name="arrived_at", lookup_expr="gte")
    arrived_at_lte = filters.DateFilter(field_name="arrived_at", lookup_expr="lte")

    class Meta:
        model = Vehicle
        fields = [
            "color",
            "arrived_at_gte",
            "arrived_at_lte",
            "license_plate",
        ]
