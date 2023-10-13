from rest_framework.response import Response
from src.apps.post_info.models import Download
from src.apps.post_info.serializers import (
    DownloadListSerializer,
    DownloadCreateSerializer,
)
from rest_framework import (
    generics,
    status,
)
from rest_framework.permissions import IsAuthenticated


class DownloadListCreateView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    def get_queryset(self):
        return Download.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DownloadListSerializer
        return DownloadCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        project = serializer.validated_data['project']
        try:
            instance = Download.objects.get(project=project, user=self.request.user)
        except Download.DoesNotExist:
            instance = serializer.save()
        instance.project.update_downloads_count()

        return Response(DownloadListSerializer(instance).data, status=status.HTTP_201_CREATED)
