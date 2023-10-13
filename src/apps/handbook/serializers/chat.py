from rest_framework import serializers
from src.apps.handbook.models import Chat
from src.apps.accounts.serializers import UserUsernameSerializer


class ChatListSerializer(serializers.ModelSerializer):

    participants = UserUsernameSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'participants',)


class ChatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id', 'participants',)

