from rest_framework.views import APIView, Request, Response, status
from .serializers import SongSerializer
from .models import Song
from django.shortcuts import get_object_or_404
from albums.models import Album


class SongAlbumView(APIView):
    def get(self, request: Request, album_id: int) -> Response:
        album = get_object_or_404(Album, pk=album_id)

        # songs = Song.objects.filter(album_id=album.id)
        songs = Song.objects.filter(album=album)
        serializer = SongSerializer(songs, many=True)

        return Response(serializer.data)

    def post(self, request: Request, album_id: int) -> Response:
        album_obj = get_object_or_404(Album, pk=album_id)

        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        song = Song.objects.create(**serializer.validated_data, album=album_obj)
        # song = Song.objects.create(**serializer.validated_data, album_id=album_obj.id)
        # song = Song.objects.create(**serializer.validated_data, album_id=album_id)

        serializer = SongSerializer(song)

        return Response(serializer.data, status.HTTP_201_CREATED)
