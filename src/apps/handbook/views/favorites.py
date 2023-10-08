from rest_framework.permissions import IsAuthenticated
from src.apps.handbook.models import Favorites
from src.apps.handbook.serializers import *
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter



class FavoritesDestroyView(generics.DestroyAPIView):
    """
    A ViewSet for destroying a single Favorite.
    """
    serializer_class = FavoritesListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Favorites.objects.filter(user=self.request.user)


class FavoritesListCreateView(generics.ListCreateAPIView):
    """
    A ViewSet for creating a single Favorite.
    """
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('project__name',)

    def get_queryset(self):
        return Favorites.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FavoritesCreateSerializer
        return FavoritesListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
