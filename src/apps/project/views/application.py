from rest_framework.response import Response
from src.apps.project.models import Application
from rest_framework.views import APIView
from src.apps.project.serializers import (
    ApplicationListSerializer,
    ApplicationCreateSerializer,
    ApplicationApproveSerializer
)
from rest_framework import (
    generics,
    status,
)
from rest_framework.permissions import IsAuthenticated


class ApplicationListCreateView(generics.ListCreateAPIView):
    
    permission_classes = (
        IsAuthenticated,
    )
    def get_queryset(self):
        return Application.objects.filter(project__user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ApplicationListSerializer
        return ApplicationCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        instance = serializer.save()

        return Response(ApplicationListSerializer(instance).data, status=status.HTTP_201_CREATED)


class ApplicationRetrieveUpdateDestroyView(generics.DestroyAPIView):
    """ Detail api view for Application model """
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Application.objects.filter(project__user=self.request.user)


class ApplicationApproveView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationApproveSerializer

    def post(self, request, *args, **kwargs):
        serializer = ApplicationApproveSerializer(data=request.data)

        if serializer.is_valid():
            for application in serializer.validated_data['applications']:
                user = application.user
                application.project.members.add(user)
                application.project.save()
                application.delete()
            return Response(
                {"detail": "All Users successfully approved"},
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": "Invalid data provided."},
            status=status.HTTP_400_BAD_REQUEST
        )
