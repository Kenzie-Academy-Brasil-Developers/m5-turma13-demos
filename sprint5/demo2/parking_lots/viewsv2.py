from rest_framework.views import APIView, Request, Response, status
from .models import ParkingLot
from .serializers import ParkingLotSerializer
from django.shortcuts import get_object_or_404
from utils.common_views import GetPostCommonView
from utils.detail_views import (
    OnlyGetDetailView,
    OnlyPatchDetailView,
    OnlyDeleteDetailView,
    GetPatchDeleteDetailView,
)

"""
    Abstração dos métodos detalhados de uma view apenas para demonstração
    de POO.
"""


class ParkingLotView(GetPostCommonView):
    view_queryset = ParkingLot.objects.all()
    view_serializer = ParkingLotSerializer


class ParkingLotDetailView(GetPatchDeleteDetailView):
    view_queryset = ParkingLot.objects.all()
    view_serializer = ParkingLotSerializer
