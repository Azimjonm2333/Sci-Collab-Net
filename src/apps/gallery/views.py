from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import *
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter


class FolderAPIView(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            self.authentication_classes = ()
        if self.action == 'retrieve':
            return FolderDetailSerializer
        return FolderSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return ()
        return (IsAuthenticated(),)


class FolderImageAPIView(generics.RetrieveAPIView):
    queryset = Folder.objects.all()
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = ('name',)
    serializer_class = FolderImageSerializer
    authentication_classes = ()


class ImageAPIView(viewsets.ModelViewSet):
    queryset = Image.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            self.authentication_classes = ()
        if self.action == 'retrieve':
            return ImageDetailSerializer
        return ImageSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return ()
        return (IsAuthenticated(),)

    # def perform_create(self, serializer):
    #     serializer.save(company=self.request.user.company)
