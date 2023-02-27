from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
import ipdb

"""
    Abstração dos métodos detalhados de uma view apenas para demonstração
    de POO.
"""


class GetDetailView:
    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        # ipdb.set_trace()
        try:
            id_value = kwargs.get(self.detail_url_id)
        except AttributeError:
            id_value = kwargs.get("pk")

        queryset = get_object_or_404(self.view_queryset, pk=id_value)
        serializer = self.view_serializer(queryset)

        return Response(serializer.data, status.HTTP_200_OK)


class PatchDetailView:
    def update(self, request: Request, *args, **kwargs) -> Response:
        try:
            id_value = kwargs.get(self.detail_url_id)
        except AttributeError:
            id_value = kwargs.get("pk")

        queryset = get_object_or_404(self.view_queryset, pk=id_value)

        serializer = self.view_serializer(queryset, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class DeleteDetailView:
    def destroy(self, request: Request, *args, **kwargs) -> Response:
        try:
            id_value = kwargs.get(self.detail_url_id)
        except AttributeError:
            id_value = kwargs.get("pk")

        queryset = get_object_or_404(self.view_queryset, pk=id_value)
        queryset.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class OnlyGetDetailView(GetDetailView, APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        return super().retrieve(request, *args, **kwargs)


class OnlyPatchDetailView(PatchDetailView, APIView):
    def patch(self, request: Request, *args, **kwargs) -> Response:
        return super().update(request, *args, **kwargs)


class OnlyDeleteDetailView(DeleteDetailView, APIView):
    def delete(self, request: Request, *args, **kwargs) -> Response:
        return super().destroy(request, *args, **kwargs)


class GetPatchDeleteDetailView(
    GetDetailView, PatchDetailView, DeleteDetailView, APIView
):
    def get(self, request: Request, *args, **kwargs) -> Response:
        return super().retrieve(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs) -> Response:
        return super().update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs) -> Response:
        return super().destroy(request, *args, **kwargs)
