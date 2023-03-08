from rest_framework import generics
from .models import Floor
from .serializers import FloorSerializer
from django.shortcuts import get_object_or_404
from parking_lots.models import ParkingLot
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from parking_lots.permissions import IsAdminOrParkingLotOwner
from parking_lots.mixins import ParkingLotPermissionMixin


class FloorView(ParkingLotPermissionMixin, generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

    parking_lot_url_kwarg = "parking_lot_id"

    def get_queryset(self):
        parking_lot_id = self.kwargs["parking_lot_id"]
        return Floor.objects.filter(parking_lot_id=parking_lot_id)

    def perform_create(self, serializer):
        parking_lot_id = self.kwargs["parking_lot_id"]
        serializer.save(parking_lot_id=parking_lot_id)
