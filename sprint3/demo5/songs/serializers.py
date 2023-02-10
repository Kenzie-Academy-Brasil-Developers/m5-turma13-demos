from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.Serializer):
    song_id = serializers.IntegerField(read_only=True, source="id")
    song_title = serializers.CharField(max_length=255, source="title")
    song_duration = serializers.DurationField(source="duration")
    # album_id = serializers.IntegerField(read_only=True)
    album_name = serializers.CharField(source="album.name", read_only=True)
