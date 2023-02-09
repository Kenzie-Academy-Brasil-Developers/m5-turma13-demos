from rest_framework import serializers
from .models import Seasons
from recipes.serializers import RecipeSerializer
from addresses.serializers import AddressSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    favorite_season = serializers.ChoiceField(
        choices=Seasons.choices,
        default=Seasons.DEFAULT,
    )
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    address = AddressSerializer()
    # recipes = RecipeSerializer(many=True, read_only=True)
