from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleCheckoutSerializer
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.views import Request, Response
from django_filters import rest_framework as filters
from .filters import VehicleFilter

"""
    ViewSet - 1
    GenericViewSet - 2
    ModelViewSet - 3
"""


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    # Se eu declaro a chave DEFAULT_FILTER_BACKENDS nos settings.py, nao preciso chamar na classe
    # filter_backends = [filters.DjangoFilterBackend]
    filterset_class = VehicleFilter
    """

    filterset_fields = ["color", "license_plate"]
    """
    # http_method_names = [
    #     "get",
    # ]

    @action(
        detail=True,
        # detail=False,
        methods=["PATCH"],
        url_path="checkout",
        serializer_class=VehicleCheckoutSerializer,
    )
    def checkout(self, request: Request, *args, **kwargs):
        vehicle: Vehicle = self.get_object()
        vehicle.checkout_vehicle()
        serializer = self.get_serializer(vehicle)

        return Response(serializer.data)
