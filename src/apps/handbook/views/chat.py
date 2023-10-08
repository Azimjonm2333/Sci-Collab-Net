from rest_framework.permissions import IsAuthenticated
from src.apps.handbook.models import Chat
from src.apps.handbook.serializers import *
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Max, F, Q


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
        return Chat.objects.filter(Q(from_user=self.request.user) | Q(to_user=self.request.user))

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ChatCreateSerializer
        return ChatListSerializer

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)


class ChatHistoryView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChatListSerializer

    def get_queryset(self):
        to_user_id = self.kwargs.get('to_user_id')
        return Chat.objects.filter(
            (Q(to_user_id=to_user_id, from_user=self.request.user) | Q(from_user_id=to_user_id, to_user=self.request.user))
        )


class ChatUserListWithLastMessageView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChatListSerializer

    def get_queryset(self):
        unique_user_pairs = Chat.objects.filter(
            Q(from_user=self.request.user) | Q(to_user=self.request.user)
        ).values('from_user', 'to_user').distinct()

        user_ids = set()
        for pair in unique_user_pairs:
            user_ids.add(pair['from_user'])
            user_ids.add(pair['to_user'])

        user_ids.remove(self.request.user.id)

        last_messages = []
        for user_id in user_ids:
            last_message = Chat.objects.filter(
                Q(from_user=self.request.user, to_user=user_id) | Q(from_user=user_id, to_user=self.request.user)
            ).latest('created_at')
            last_messages.append(last_message)

        return last_messages