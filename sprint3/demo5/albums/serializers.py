from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Album


class AlbumSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=127)
    year = serializers.IntegerField(min_value=1, max_value=9999)
    serial_number = serializers.IntegerField(
        validators=[
            UniqueValidator(Album.objects.all(), message="Esse campo deve ser unico"),
        ]
    )

    # album_duration = serializers.CharField(
    #     source="total_album_duration", read_only=True
    # )
    album_duration = serializers.DurationField(
        source="total_album_duration", read_only=True
    )
