from django.urls import path
from .views import ParkingLotView, ParkingLotDetailView
from floors.views import FloorView
from vehicles.views import VehicleView, VehicleCheckoutView

urlpatterns = [
    path("parking-lots/", ParkingLotView.as_view()),
    path("parking-lots/<int:parking_lot_id>/", ParkingLotDetailView.as_view()),
    path("parking-lots/<int:parking_lot_id>/floors/", FloorView.as_view()),
    path("parking-lots/<int:parking_lot_id>/vehicles/", VehicleView.as_view()),
    path(
        "parking-lots/<int:parking_lot_id>/vehicles/<int:vehicle_id>/checkout/",
        VehicleCheckoutView.as_view(),
    ),
]
