from django.urls import path
from .views import ParkingLotView, ParkingLotDetailView


urlpatterns = [
    path("parking-lots/", ParkingLotView.as_view()),
    path("parking-lots/<int:parking_lot_id>/", ParkingLotDetailView.as_view()),
]
