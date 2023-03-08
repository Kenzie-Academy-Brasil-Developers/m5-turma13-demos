from rest_framework import generics
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleCheckoutSerializer, ReportSerializer
from rest_framework.permissions import IsAuthenticated
from parking_lots.permissions import IsAdminOrParkingLotOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from parking_lots.mixins import ParkingLotPermissionMixin
from floors.models import Spot
from rest_framework.exceptions import NotFound
from django.utils import timezone


"""
    Profiling
"""


class ReportView(generics.ListAPIView):
    # evaluted / query de schrodinger
    queryset = Vehicle.objects.all()
    serializer_class = ReportSerializer

    parking_lot_url_kwarg = "parking_lot_id"

    def get_queryset(self):
        parking_lot_id = self.kwargs[self.parking_lot_url_kwarg]

        queryset = self.queryset.filter(spot__floor__parking_lot_id=parking_lot_id)
        # select_related só pode ser usado em campos de relacionamento do lado N (1:N)
        # prefetch_related só pode ser usado em lado N (N:N)
        queryset = queryset.select_related("spot")
        queryset = queryset.select_related("spot__floor__parking_lot")
        queryset = queryset.select_related("spot__floor__parking_lot__account")

        return queryset


class VehicleCheckoutView(ParkingLotPermissionMixin, generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    queryset = Vehicle.objects.all()
    serializer_class = VehicleCheckoutSerializer

    parking_lot_url_kwarg = "parking_lot_id"

    def get_object(self):
        """
        1. Estacionamento existe?
        2. Carro existe no estacionamento achado
        3. Pagamento
            3.1 - Atualizar o atributo paid_at com o timestamp now
            3.2 - Calcular o intervalo entre arrived_at e paid_at
            3.3 - Calcular o preço com base no intervalo
        """
        vehicle_id = self.kwargs["vehicle_id"]
        parking_lot_id = self.kwargs[self.parking_lot_url_kwarg]

        vehicle_found = Vehicle.objects.filter(
            id=vehicle_id,
            spot__floor__parking_lot_id=parking_lot_id,
            spot__is_free=False,
        ).first()

        if not vehicle_found:
            raise NotFound("Car not found.")

        import ipdb

        # ipdb.set_trace()
        vehicle_found.paid_at = timezone.now()
        time_elapsed = vehicle_found.paid_at - vehicle_found.arrived_at
        seconds = time_elapsed.total_seconds()

        vehicle_found.amound_paid = seconds * 5
        vehicle_found.spot.is_free = True
        vehicle_found.spot.save()

        return vehicle_found


class VehicleView(ParkingLotPermissionMixin, generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    parking_lot_url_kwarg = "parking_lot_id"

    def get_queryset(self):
        parking_lot_id = self.kwargs[self.parking_lot_url_kwarg]

        return Vehicle.objects.filter(
            spot__floor__parking_lot_id=parking_lot_id, spot__is_free=False
        )

    def perform_create(self, serializer):
        """
        1. Estacionamento existe?
        2. Achar a vaga mais adequada
            2.1 - Caso não exista, retornar que nao existem vagas para o vehicle_type
            2.2 - Filtrar por prioridade do piso (spot_priority)
            2.3 - Verificar se existem vagas disponiveis para o tipo especifico
            2.4 - Achada a vaga, trocar seu status para ocupado (is_free=False)
        """
        """
            SELECT
                ff."name", ff.spot_priority, sp.*
            FROM
                floors_floor ff
            JOIN
                parking_lots_parkinglot plp
                ON ff.parking_lot_id = plp.id
            JOIN
                floors_spot sp
                ON sp.floor_id = ff.id
            WHERE
                plp.id = 2
                AND sp.variety = 'car'
                AND sp.is_free IS TRUE
            ORDER BY
                ff.spot_priority
            LIMIT 1;
        """

        # field lookups
        parking_lot_id = self.kwargs[self.parking_lot_url_kwarg]
        vehicle_type = serializer.validated_data["vehicle_type"]

        found_spot = (
            Spot.objects.filter(
                floor__parking_lot_id=parking_lot_id,
                is_free=True,
                variety=vehicle_type,
            )
            .order_by("floor__spot_priority")
            .first()
        )

        if not found_spot:
            raise NotFound("Vaga não encontrada.")

        found_spot.is_free = False
        found_spot.save()

        serializer.save(spot=found_spot)
