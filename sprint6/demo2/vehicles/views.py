from rest_framework import generics
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.permissions import IsAuthenticated
from parking_lots.permissions import IsAdminOrParkingLotOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from parking_lots.models import ParkingLot
from parking_lots.mixins import ParkingLotPermissionMixin
from floors.models import Spot
from rest_framework.exceptions import NotFound


class VehicleView(ParkingLotPermissionMixin, generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    parking_lot_url_kwarg = "parking_lot_id"

    def get_queryset(self):
        """
        - Precisa estar autenticado pra criar/listar
        has_permission / has_object_permission
        - Somente ADMIN ou DONO do parking lot possa listar os pisos
        - Somente ADMIN ou DONO do parking lot possa criar o piso
        """
        # 1. Verificar se o estacionamento existe
        parking_lot_obj = get_object_or_404(
            ParkingLot, pk=self.kwargs["parking_lot_id"]
        )
        # 2. Verificar se o usuario é admin ou dono
        self.check_object_permissions(self.request, parking_lot_obj)

        # TODO:
        """
            Fazer o caminho até o parking lot, passando por
            1. spot
            2. floor
            3. parking lot
        """
        return Vehicle.objects.filter(parking_lot=parking_lot_obj)

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
        parking_lot_id = self.kwargs["parking_lot_id"]
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
            raise NotFound

        found_spot.is_free = False
        found_spot.save()

        serializer.save(spot=found_spot)
