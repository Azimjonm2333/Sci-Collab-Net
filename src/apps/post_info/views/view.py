from rest_framework.response import Response
from src.apps.post_info.models import View
from src.apps.post_info.serializers import (
    ViewListSerializer,
    ViewCreateSerializer,
)
from rest_framework import (
    generics,
    status,
)
from rest_framework.permissions import IsAuthenticated


class ViewListCreateView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    def get_queryset(self):
        return View.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ViewListSerializer
        return ViewCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        project = serializer.validated_data['project']
        try:
            instance = View.objects.get(project=project, user=self.request.user)
        except View.DoesNotExist:
            instance = serializer.save()
        instance.project.update_views_count()

        return Response(ViewListSerializer(instance).data, status=status.HTTP_201_CREATED)
