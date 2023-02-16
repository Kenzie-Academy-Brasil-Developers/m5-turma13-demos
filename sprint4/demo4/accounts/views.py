from rest_framework.views import APIView, Request, Response, status
from .models import Account
from .serializers import AccountSerializer, LoginSerializer, CustomJWTSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# MRO (Method Resolution Order)
class LoginView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


"""
class LoginViewOld2(APIView):
    def post(self, request: Request) -> Response:
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status.HTTP_200_OK)


class LoginViewOld1(APIView):

    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        # user = authenticate(**serializer.validated_data)

        if not user:
            return Response(
                {"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN
            )

        refresh = RefreshToken.for_user(user)
        return_dict = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(return_dict, status.HTTP_200_OK)
"""


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
