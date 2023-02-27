from rest_framework import generics
from .models import Floor
from .serializers import FloorSerializer
from django.shortcuts import get_object_or_404
from parking_lots.models import ParkingLot
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from parking_lots.permissions import IsAdminOrParkingLotOwner


class FloorView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

    """
    - Precisa estar autenticado pra criar/listar
    has_permission / has_object_permission
    - Somente ADMIN ou DONO do parking lot possa listar os pisos
    - Somente ADMIN ou DONO do parking lot possa criar o piso
    """

    def get_queryset(self):
        parking_lot_obj = get_object_or_404(
            ParkingLot, pk=self.kwargs["parking_lot_id"]
        )
        self.check_object_permissions(self.request, parking_lot_obj)

        return Floor.objects.filter(parking_lot=parking_lot_obj)

    def perform_create(self, serializer):
        import ipdb

        # ipdb.set_trace()
        # 1. Verificar se o estacionamento existe
        parking_lot_obj = get_object_or_404(
            ParkingLot, pk=self.kwargs["parking_lot_id"]
        )
        self.check_object_permissions(self.request, parking_lot_obj)

        serializer.save(parking_lot=parking_lot_obj)
