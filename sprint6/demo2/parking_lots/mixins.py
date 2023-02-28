from django.shortcuts import get_object_or_404
from .models import ParkingLot


class ParkingLotPermissionMixin:
    parking_lot_url_kwarg = None

    def check_custom_object_permission(self):
        assert self.parking_lot_url_kwarg is not None, (
            "'%s' should include a `parking_lot_url_kwarg` attribute"
            % self.__class__.__name__
        )

        parking_lot_id = self.kwargs[self.parking_lot_url_kwarg]
        parking_lot_obj = get_object_or_404(ParkingLot, pk=parking_lot_id)

        self.check_object_permissions(self.request, parking_lot_obj)

    def get(self, request, *args, **kwargs):
        self.check_custom_object_permission()

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.check_custom_object_permission()
        return self.create(request, *args, **kwargs)
