from rest_framework import serializers
from src.apps.handbook.models import Chat
from src.apps.accounts.serializers import UserShortSerializer


class ChatListSerializer(serializers.ModelSerializer):

    from_user = UserShortSerializer()
    to_user = UserShortSerializer()

    class Meta:
        model = Chat
        fields = ('id', 'from_user', 'to_user', 'message',)

class ChatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'to_user', 'message',)

class ChatUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'message',)
