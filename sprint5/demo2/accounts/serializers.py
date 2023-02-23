from rest_framework import serializers
from .models import Account, ShiftOptions
from rest_framework.validators import UniqueValidator

"""
    ModelSerializer:
        - Já vem com .create e .update nativos (sua versão mais generica)
            - model.objects.create(**validated_data)
"""


def choices_error_message(choices_class):
    valid_choices = [choice[0] for choice in choices_class.choices]
    message = ", ".join(valid_choices).rsplit(",", 1)

    return "Choose between " + " and".join(message) + "."


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
        extra_kwargs = {
            "password": {"write_only": True},
            "shift": {
                "error_messages": {
                    "invalid_choice": choices_error_message(ShiftOptions),
                }
            },
            # Atenção, sobrescrever validators no extra_kwargs elimina toda regra
            # mapeada do campo da model pelo ModelSerializer, não é recomendado fazer isso
            # "email": {
            #     "validators": [
            #         UniqueValidator(
            #             queryset=Account.objects.all(), message="mensagem de erro"
            #         )
            #     ]
            # },
        }
        # fields = "__all__"
