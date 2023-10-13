from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.apps.handbook.serializers import *
from src.apps.handbook.models import Message, Chat
from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import Q




def get_chat_with_user(user1_id, user2_id):
    chat = Message.objects.none()
    chats = Chat.objects.filter(Q(participants=user2_id) | Q(participants=user1_id)).distinct().prefetch_related('participants')
    for x in chats:
        if len(x.participants.all()) == 2:
            chat = x
            break
    return Message.objects.filter(chat=chat).distinct() if chat else chat



class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    A ViewSet for Retrieve Update Destroy a single Message.
    """
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Message.objects.filter(chat__participants=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MessageCreateSerializer
        return MessageUpdateSerializer




class MessageListCreateView(generics.ListCreateAPIView):
    """
    A ViewSet for creating a single Message.
    """
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ('message',)

    def get_queryset(self):
        return Message.objects.filter(chat__participants=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MessageCreateSerializer
        return MessageListSerializer


    def create(self, serializer):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(sender=self.request.user)

        return Response(MessageListSerializer(instance).data, status=status.HTTP_201_CREATED)



class MessageHistoryView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageListSerializer

    def get_queryset(self):
        to_user_id = self.kwargs.get('to_user_id')
        messages = get_chat_with_user(to_user_id, self.request.user.id)
        return messages


class MessageUserListWithLastMessageView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageListSerializer

    def get_queryset(self):
        unique_user_pairs = Message.objects.filter(chat__participants=1).distinct()

        chats = {}
        for pair in unique_user_pairs:
            chats[pair.chat.id] = pair
        last_messages = list(chats.values())

        return last_messages
