from rest_framework.views import APIView, Request, Response, status
from .serializers import BookSerializer
from .models import Book


class BookView(APIView):
    def get(self, request: Request) -> Response:
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        # 1
        serializer = BookSerializer(data=request.data)
        # 2
        serializer.is_valid(raise_exception=True)

        # Chama o método .create (se a instancia foi criada apenas com data=)
        # serializer.save()
        serializer.save()

        # # 3
        # book = Book.objects.create(**serializer.validated_data)

        # # 4
        # serializer = BookSerializer(book)

        # 5
        return Response(serializer.data, status.HTTP_201_CREATED)
