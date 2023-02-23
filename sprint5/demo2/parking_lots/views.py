from .models import ParkingLot
from .serializers import ParkingLotSerializer
from rest_framework import generics


class ParkingLotView(generics.ListCreateAPIView):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer


class ParkingLotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

    lookup_url_kwarg = "parking_lot_id"
