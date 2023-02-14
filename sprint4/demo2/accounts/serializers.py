from rest_framework import serializers
from .models import Account
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["cpf"] = user.cpf

        return token


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=127, write_only=True)
    cpf = serializers.CharField(max_length=11, allow_null=True, default=None)
    birthdate = serializers.DateField(allow_null=True, default=None)

    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(max_length=127, write_only=True)
