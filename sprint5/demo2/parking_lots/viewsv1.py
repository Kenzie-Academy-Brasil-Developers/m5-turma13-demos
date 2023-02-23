from rest_framework.views import APIView, Request, Response, status
from .models import ParkingLot
from .serializers import ParkingLotSerializer
from django.shortcuts import get_object_or_404

"""
    Versão inicial com APIView.
"""


class ParkingLotView(APIView):
    def get(self, request: Request) -> Response:
        # 1
        parking_lots = ParkingLot.objects.all()
        # 2
        serializer = ParkingLotSerializer(parking_lots, many=True)

        # 3
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        # 1
        serializer = ParkingLotSerializer(data=request.data)
        # 2
        serializer.is_valid(raise_exception=True)
        # 3
        serializer.save()
        # 4
        return Response(serializer.data, status.HTTP_201_CREATED)


class ParkingLotDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        parking_lot = get_object_or_404(ParkingLot, pk=pk)
        serializer = ParkingLotSerializer(parking_lot)

        return Response(serializer.data, status.HTTP_200_OK)
        # parking_lot = get_object_or_404(ParkingLot, id=pk)

    def patch(self, request: Request, pk: int) -> Response:
        parking_lot = get_object_or_404(ParkingLot, pk=pk)

        serializer = ParkingLotSerializer(parking_lot, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
        # parking_lot = get_object_or_404(ParkingLot, id=pk)

    def delete(self, request: Request, pk: int) -> Response:
        parking_lot = get_object_or_404(ParkingLot, pk=pk)
        parking_lot.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        # parking_lot = get_object_or_404(ParkingLot, id=pk)
