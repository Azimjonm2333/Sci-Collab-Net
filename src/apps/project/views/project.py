from rest_framework.response import Response
from src.apps.project.models import Project

from src.apps.project.serializers import (
    ProjectListSerializer,
    ProjectCreateSerializer,
    ProjectDetailSerializer,
    ProjectUpdateSerializer,
)
from rest_framework import (
    generics,
    status,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.permissions import IsAuthenticated



class ProjectListCreateView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
    )
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = (
        'name',
    )

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjectListSerializer
        return ProjectCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return Response(ProjectDetailSerializer(instance).data, status=status.HTTP_201_CREATED)


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """ Detail api view for Project model """
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProjectListSerializer
        return ProjectUpdateSerializer
