from rest_framework.views import APIView, Request, Response, status
from .serializers import BookSerializer, BookMarkSerializer
from .models import Book, BookMark
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404
from .permissions import IsBookOwner


class BookView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request) -> Response:
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(owner=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class BookDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly, IsBookOwner]

    def get(self, request: Request, book_id: int) -> Response:
        book = get_object_or_404(Book, pk=book_id)

        serializer = BookSerializer(book)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, book_id: int) -> Response:
        book = get_object_or_404(Book, pk=book_id)
        self.check_object_permissions(request, book)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, book_id: int) -> Response:
        """
        1. Tem token? 401
        2. É token de admin? 403
        3. Livro existe? 404
        4. Usuario do token é dono do livro? 403
        """
        book = get_object_or_404(Book, pk=book_id)
        self.check_object_permissions(request, book)

        serializer = BookSerializer(book, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class BookMarkView(APIView):
    def get(self, request: Request, book_id: int) -> Response:
        book_obj = get_object_or_404(Book, pk=book_id)
        bookmarks = BookMark.objects.filter(book=book_obj)

        serializer = BookMarkSerializer(bookmarks, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
