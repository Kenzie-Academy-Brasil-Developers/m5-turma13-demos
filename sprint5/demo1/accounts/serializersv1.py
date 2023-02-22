from rest_framework import serializers
from .models import Account, ShiftOptions
from rest_framework.validators import UniqueValidator


class AccountSerializerV1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    shift = serializers.ChoiceField(
        choices=ShiftOptions.choices,
        default=ShiftOptions.DEFAULT,
    )
    password = serializers.CharField(max_length=150, write_only=True)
    first_name = serializers.CharField(max_length=127)
    last_name = serializers.CharField(max_length=127)

    username = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(
                Account.objects.all(), "A user with that username already exists."
            ),
        ],
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                Account.objects.all(), "A user with that email already exists."
            ),
        ],
    )

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
