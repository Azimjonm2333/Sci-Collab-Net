from rest_framework.permissions import IsAuthenticated
from src.apps.handbook.models import Chat
from src.apps.handbook.serializers import *
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter



class ChatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    A ViewSet for Retrieve Update Destroy a single Favorite.
    """
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Chat.objects.filter(from_user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ChatCreateSerializer
        return ChatUpdateSerializer


class ChatListCreateView(generics.ListCreateAPIView):
    """
    A ViewSet for creating a single Favorite.
    """
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('project__name',)

    def get_queryset(self):
        return Chat.objects.filter(from_user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ChatCreateSerializer
        return ChatListSerializer

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)
