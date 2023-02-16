from rest_framework import permissions
import ipdb
from rest_framework.views import Request, View
from .models import Book


class IsBookOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, book: Book) -> bool:
        print("IsBookOwner executado")
        # ipdb.set_trace()
        # if book.owner == request.user:
        #     return True
        # return False

        # return request.user.is_superuser or book.owner == request.user
        return book.owner == request.user
