from rest_framework import permissions
from rest_framework.views import Request, View
from accounts.models import Account


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Account):
        return request.user == obj
