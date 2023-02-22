from rest_framework import serializers
from .models import Account


"""
    ModelSerializer:
        - Já vem com .create e .update nativos (sua versão mais generica)
            - model.objects.create(**validated_data)
"""


class AccountSerializer(serializers.ModelSerializer):
    """
    TODO:
    - Voltar opções válidas quando shift for enviado errado.
    """

    # password = serializers.CharField(max_length=150, write_only=True)

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        """
        Falta implementar a parte de hashear o password, caso seja passado
        """
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Account
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "shift",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        # fields = "__all__"
