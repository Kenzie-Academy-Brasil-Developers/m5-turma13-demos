from rest_framework.views import APIView, Request, Response, status
from .models import User
import ipdb
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        # QuerySet
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        # Trazer também as receitas do usuario

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        # Validando e limpando a entrada
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(**serializer.validated_data)

        # Formatando o objeto para saída
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)
