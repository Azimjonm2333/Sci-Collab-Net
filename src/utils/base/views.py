from rest_framework import status, viewsets
from rest_framework.response import Response


class BaseAPIView(viewsets.ModelViewSet):
    """ Base API view with operations CRUD for model exchange rate """

    list_serializer = None
    detail_serializer = None
    create_serializer = None
    update_serializer = None

    tag = None
    def get_list_serializer(self):
        if self.list_serializer is None:
            return self.get_serializer_class()
        return self.list_serializer

    def get_create_serializer(self):
        if self.create_serializer is None:
            return self.get_serializer_class()
        return self.create_serializer

    def get_update_serializer(self):
        if self.update_serializer is None:
            return self.get_serializer_class()
        return self.update_serializer

    def get_detail_serializer(self):
        if self.detail_serializer is None:
            return self.get_serializer_class()
        return self.detail_serializer

    def get_serializer_class(self):

        if self.action == 'list':
            return self.get_list_serializer()

        if self.action == 'retrieve':
            return self.get_detail_serializer()

        if self.action == 'update' or self.action == 'patch':
            return self.get_update_serializer()

        return self.get_create_serializer()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(self.get_detail_serializer()(instance).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(self.get_detail_serializer()(instance).data)