from rest_framework.views import APIView, Request, Response, status
from .serializers import BookSerializer
from .models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from accounts.permissions import IsAdminOrReadOnly


# Autenticação -> diz sobre QUEM está acessando a rota
# Permissão / Autorização -> restringe o acesso a determinado recurso
class BookView(APIView):
    authentication_classes = [JWTAuthentication]
    """
    , -> AND
    | -> OR
    """
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request) -> Response:
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        import ipdb

        # ipdb.set_trace()

        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # serializer.save(owner=request.user)
        serializer.save(owner_id=request.user.id)

        return Response(serializer.data, status.HTTP_201_CREATED)
