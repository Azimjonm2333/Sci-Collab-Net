from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException
from src.apps.handbook.models import Category



class CategoriesParentStatus(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Нужно добавить только те категории у которых нету дочерей"

class UserProfileAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserProfileDetailSerializer
        return UserProfileUpdateSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.request.user
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        user_obj = self.request.user

        instance = UserProfile.objects.get(user=user_obj)

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance, data=request.data, partial=True)

        if serializer.is_valid():
            categories = serializer.validated_data.get("categories", False)
            if categories:
                for category in categories:
                    if Category.objects.filter(parent=category):
                        raise CategoriesParentStatus

            serializer.save()
            return Response({
                "detail": "Ваш профиль успешно обновлён",
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            instance = UserProfile.objects.get(user=request.user)
            return Response(UserProfileDetailSerializer(instance).data, status=status.HTTP_200_OK)

        except UserProfile.DoesNotExist:
            return Response({"detail": "Профиль пользователя не найден"}, status=status.HTTP_404_NOT_FOUND)
