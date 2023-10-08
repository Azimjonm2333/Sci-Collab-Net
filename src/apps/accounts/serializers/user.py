from rest_framework import serializers
from ..models import User, UserProfile


class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'username',
            'phone',
            'email',
        )


class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class UserUsernameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )


class UserProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
            'avatar',
            'first_name',
            'last_name',
            'categories',
            'description'
        )


class UserProfileDetailSerializer(serializers.ModelSerializer):
    
    user = UserListSerializer()
    
    class Meta:
        model = UserProfile
        fields = (
            'avatar',
            'first_name',
            'last_name',
            'categories',
            'description',
            'user'
        )
