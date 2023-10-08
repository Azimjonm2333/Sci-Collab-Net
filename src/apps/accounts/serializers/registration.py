import random
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from ..models import User


class ChangePasswordSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    old_password = serializers.CharField(min_length=8)
    new_password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Не найдено пользователь с этим Юзером")
        return value

    def validate(self, data):
        username = data.get('username')
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        password_confirmation = data.get('password_confirmation')

        if not check_password(old_password, User.objects.get(username=username).password):
            raise serializers.ValidationError("Старый пароль не верный")
        if new_password and new_password != password_confirmation:
            raise serializers.ValidationError("Пароли не совпадают")
        return data


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone',
            'password',
            'password_confirmation',
        )

    def validate(self, data):
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password and password != password_confirmation:
            raise serializers.ValidationError("Пароли не совпадают")
        for symbol in password:
            if ord('!') > ord(symbol) or ord(symbol) > ord('~'):
                raise serializers.ValidationError("Недоступные символы")
        return data

    def save(self, **kwargs):
        assert hasattr(self, '_errors'), (
            'You must call `.is_valid()` before calling `.save()`.'
        )

        assert not self.errors, (
            'You cannot call `.save()` on a serializer with invalid data.'
        )

        # Guard against incorrect use of `serializer.save(commit=False)`
        assert 'commit' not in kwargs, (
            "'commit' is not a valid keyword argument to the 'save()' method. "
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
            "You can also pass additional keyword arguments to 'save()' if you "
            "need to set extra attributes on the saved model instance. "
            "For example: 'serializer.save(owner=request.user)'.'"
        )

        assert not hasattr(self, '_data'), (
            "You cannot call `.save()` after accessing `serializer.data`."
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
        )

        self.validated_data.pop('password_confirmation')
        instance = User.objects.create_client(**self.validated_data)

        return instance


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )
