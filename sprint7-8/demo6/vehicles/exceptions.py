from rest_framework.exceptions import APIException
from rest_framework.views import status


class CheckoutError(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_message = "Vehicle already checked-out."

    def __init__(self, detail=None, code=None):
        self.detail = detail or self.default_message
