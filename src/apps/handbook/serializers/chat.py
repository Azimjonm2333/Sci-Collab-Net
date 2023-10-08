from rest_framework import serializers
from src.apps.handbook.models import Chat
from src.apps.accounts.serializers import UserUsernameSerializer


class ChatListSerializer(serializers.ModelSerializer):

    from_user = UserUsernameSerializer()
    to_user = UserUsernameSerializer()

    class Meta:
        model = Chat
        fields = ('id', 'from_user', 'to_user', 'message', 'created_at', 'updated_at',)

class ChatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'to_user', 'message',)

class ChatUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'message',)
