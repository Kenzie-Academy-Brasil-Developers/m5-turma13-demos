from rest_framework.views import APIView, Request, Response, status
from .serializers import BookSerializer
from .models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated


class BookView(APIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request) -> Response:
        print("=" * 100)
        print("METODO GET EXECUTADO")
        print("=" * 100)
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        import ipdb

        # ipdb.set_trace()

        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
