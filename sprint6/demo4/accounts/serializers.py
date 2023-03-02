from rest_framework import serializers
from .models import Account, ShiftOptions

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
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "shift": {
                "error_messages": {
                    "invalid_choice": choices_error_message(ShiftOptions),
                }
            },
        }
