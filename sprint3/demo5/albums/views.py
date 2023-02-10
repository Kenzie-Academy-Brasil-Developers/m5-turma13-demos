from rest_framework.views import APIView, Request, Response, status
from .models import Album
from .serializers import AlbumSerializer


class AlbumView(APIView):
    def get(self, request: Request) -> Response:
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        album = Album.objects.create(**serializer.validated_data)

        serializer = AlbumSerializer(album)

        return Response(serializer.data, status.HTTP_201_CREATED)
