from rest_framework.views import APIView, Request, Response, status

"""
    Abstração dos métodos gerais de uma view apenas para demonstração
    de POO.
"""

class GetCommonView:
    def list(self, request: Request) -> Response:
        # 1
        queryset = self.view_queryset.all()
        # 2
        serializer = self.view_serializer(queryset, many=True)

        # 3
        return Response(serializer.data, status.HTTP_200_OK)


class PostCommonView:
    def create(self, request: Request) -> Response:
        # 1
        serializer = self.view_serializer(data=request.data)
        # 2
        serializer.is_valid(raise_exception=True)
        # 3
        serializer.save()
        # 4
        return Response(serializer.data, status.HTTP_201_CREATED)


class OnlyPostCommonView(PostCommonView, APIView):
    def post(self, request: Request) -> Response:
        return super().create(request)


class OnlyGetCommonView(PostCommonView, APIView):
    def get(self, request: Request) -> Response:
        return super().llist(request)


class GetPostCommonView(GetCommonView, PostCommonView, APIView):
    def get(self, request: Request) -> Response:
        return super().list(request)

    def post(self, request: Request) -> Response:
        return super().create(request)
