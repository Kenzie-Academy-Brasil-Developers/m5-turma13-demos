from rest_framework.views import APIView, Request, Response, status
from .models import Account
from .serializers import AccountSerializer
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


class AccountView(GetPostCommonView):
    view_queryset = Account.objects.all()
    view_serializer = AccountSerializer


class AccountDetailView(GetPatchDeleteDetailView):
    view_queryset = Account.objects.all()
    view_serializer = AccountSerializer

    detail_url_id = "account_id"
