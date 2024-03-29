from rest_framework.views import APIView, Request, Response, status
from .models import Account
from .serializers import AccountSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @extend_schema(
        operation_id="accounts_list",
        responses={200: AccountSerializer},
        description="Rota para listagem de contas",
        summary="Sumario Listagem de Contas",
        tags=["Tag Listagem de Contas"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    lookup_url_kwarg = "account_id"
