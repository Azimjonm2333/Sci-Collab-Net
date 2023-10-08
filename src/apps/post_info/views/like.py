from rest_framework.response import Response
from src.apps.post_info.models import Like
from rest_framework.views import APIView
from src.apps.post_info.serializers import (
    LikeListSerializer,
    LikeCreateSerializer,
)
from rest_framework import (
    generics,
    status,
)
from rest_framework.permissions import IsAuthenticated


class LikeListCreateView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LikeListSerializer
        return LikeCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        project = serializer.validated_data['project']
        try:
            instance = Like.objects.get(project=project,user=self.request.user)
            instance.delete()
        except Like.DoesNotExist:
            instance = serializer.save()
        instance.project.update_likes_count()

        return Response(LikeListSerializer(instance).data, status=status.HTTP_201_CREATED)
