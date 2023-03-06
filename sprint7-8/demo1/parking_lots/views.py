from .models import ParkingLot
from .serializers import ParkingLotSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrParkingLotOwner


class ParkingLotView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

    def get_queryset(self):
        """
        - Se for superuser, lista todos os estacionamentos.
        - Se não for, lista apenas os seus.
        """
        if self.request.user.is_superuser:
            return ParkingLot.objects.all()

        return ParkingLot.objects.filter(
            account=self.request.user,
            is_active=True,
        )

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class ParkingLotDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    queryset = ParkingLot.objects.all()
    serializer_class = ParkingLotSerializer

    lookup_url_kwarg = "parking_lot_id"

    def perform_destroy(self, instance: ParkingLot):
        instance.is_active = False
        instance.save()
