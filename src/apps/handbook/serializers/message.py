from rest_framework import serializers
from src.apps.handbook.models import Message, Chat
from src.apps.accounts.serializers import UserUsernameSerializer
from src.apps.accounts.models import User
from django.db.models import Q



def get_chat_with_user(user1_id, user2_id):
    chat = Message.objects.none()
    chats = Chat.objects.filter(Q(participants=user2_id) | Q(participants=user1_id)).distinct().prefetch_related('participants')
    for x in chats:
        if len(x.participants.all()) == 2:
            chat = x
            break
    return chat


class MessageListSerializer(serializers.ModelSerializer):

    # chat = ChatListSerializer()
    sender = UserUsernameSerializer()

    class Meta:
        model = Message
        fields = ('id', 'chat', 'sender', 'message', 'created_at', 'updated_at',)


class MessageCreateSerializer(serializers.ModelSerializer):
    recipient = serializers.IntegerField()

    class Meta:
        model = Message
        fields = ('id', 'recipient', 'message',)

    def validate_recipient(self, value):
        try:
            user = User.objects.get(id=value)
            return user
        except User.DoesNotExist:
            raise serializers.ValidationError("Данного пользователя не существует")

    def create(self, validated_data: dict):
        user = validated_data['sender']
        recipient = validated_data.pop('recipient')
        chat = get_chat_with_user(user, recipient)

        if not chat:
            chat = Chat.objects.create()
            chat.participants.set([user, recipient])
            chat.save()

        validated_data['chat'] = chat
        message = Message.objects.create(**validated_data)

        return message




class MessageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'message',)
