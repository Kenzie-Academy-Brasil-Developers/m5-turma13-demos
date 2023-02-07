from rest_framework.views import APIView, Request, Response, status
from .models import User
from django.forms.models import model_to_dict
import ipdb
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        # QuerySet
        users = User.objects.all()

        # ipdb.set_trace()

        user_list = []
        for user in users:
            user_dict = model_to_dict(user)
            user_dict["updated_at"] = user.updated_at
            user_dict["created_at"] = user.created_at
            user_dict["recipes"] = [
                model_to_dict(recipe) for recipe in user.recipes.all()
            ]

            user_list.append(user_dict)

        return Response(user_list)

    def post(self, request: Request) -> Response:
        # Validando e limpando a entrada
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(**serializer.validated_data)

        # Formatando o objeto para saída
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)
