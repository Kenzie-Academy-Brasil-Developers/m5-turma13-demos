from rest_framework.views import APIView, Request, Response, status
from .models import User
import ipdb
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from addresses.models import Address


class UserView(APIView):
    def get(self, request: Request) -> Response:
        # QuerySet
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        # Validando e limpando a entrada
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        """
            1. Separar os dados de usuário e de endereço
            2. Criar o lado que não depende do outro (user)
            3. Criar o lado que depende do outro (address), associando com user
        """

        address_data = serializer.validated_data.pop("address")
        user_obj = User.objects.create(**serializer.validated_data)
        Address.objects.create(**address_data, user=user_obj)

        # Formatando o objeto para saída
        serializer = UserSerializer(user_obj)

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        # try:
        #     user = User.objects.get(id=user_id)
        # except User.DoesNotExist:
        #     return Response({"detail": "Not Found."}, status.HTTP_404_NOT_FOUND)

        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        serializer = UserSerializer(data=request.data, partial=True)

        # if not serializer.is_valid():
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)

        for key, value in serializer.validated_data.items():
            setattr(user, key, value)

        user.save()

        serializer = UserSerializer(user)

        return Response(serializer.data)

    def delete(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
