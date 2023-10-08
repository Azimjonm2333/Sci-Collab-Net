from rest_framework import serializers
from src.apps.handbook.models import Favorites
from src.apps.project.serializers import ProjectListSerializer
from src.apps.accounts.serializers import UserListSerializer


class FavoritesListSerializer(serializers.ModelSerializer):

    user = UserListSerializer()

    class Meta:
        model = Favorites
        fields = ('id', 'project', 'user',)


class FavoritesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = ('id', 'project',)
