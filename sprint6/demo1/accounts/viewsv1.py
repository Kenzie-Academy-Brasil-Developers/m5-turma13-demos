from rest_framework.views import APIView, Request, Response, status
from .models import Account
from .serializers import AccountSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner

"""
    Versão inicial com APIView.
"""


class AccountView(APIView):
    def get(self, request: Request) -> Response:
        # 1
        accounts = Account.objects.all()
        # 2
        serializer = AccountSerializer(accounts, many=True)

        # 3
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        # 1
        serializer = AccountSerializer(data=request.data)
        # 2
        serializer.is_valid(raise_exception=True)
        # 3
        serializer.save()
        # 4
        return Response(serializer.data, status.HTTP_201_CREATED)


class AccountDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    def get(self, request: Request, pk: int) -> Response:
        account = get_object_or_404(Account, pk=pk)
        self.check_object_permissions(request, account)

        serializer = AccountSerializer(account)

        return Response(serializer.data, status.HTTP_200_OK)
        # account = get_object_or_404(Account, id=pk)

    def patch(self, request: Request, pk: int) -> Response:
        account = get_object_or_404(Account, pk=pk)
        self.check_object_permissions(request, account)

        serializer = AccountSerializer(account, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
        # account = get_object_or_404(Account, id=pk)

    def delete(self, request: Request, pk: int) -> Response:
        account = get_object_or_404(Account, pk=pk)
        self.check_object_permissions(request, account)
        account.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        # account = get_object_or_404(Account, id=pk)
