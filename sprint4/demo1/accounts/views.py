from rest_framework.views import APIView, Request, Response, status
from .models import Account
from .serializers import AccountSerializer


class AccountView(APIView):
    def get(self, request: Request) -> Response:
        accounts = Account.objects.all()

        serializer = AccountSerializer(accounts, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        # 1
        serializer = AccountSerializer(data=request.data)
        # 2
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # # 3
        # account = Account.objects.create_user(**serializer.validated_data)

        # # 4
        # serializer = AccountSerializer(account)

        # 5
        return Response(serializer.data, status.HTTP_201_CREATED)
