from rest_framework import serializers
from src.apps.handbook.models import Tag


class TagListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug',)


class TagDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['name', 'slug', 'created_at', 'updated_at']