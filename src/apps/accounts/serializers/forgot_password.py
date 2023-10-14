from random import randint
from rest_framework import serializers
from ..models import User
from src.utils.functions import send_email_notification


class ForgotPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = (
            'email',
        )

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Электронной почты не существует.")
        return value

    def create(self, validated_data):
        otp = randint(10000, 99999)
        instance = User.objects.get(
            email=validated_data['email']
        )
        instance.otp = otp
        instance.save()
        subject = "Восстановления пароля"
        message = f"Код для восстановления пароля - {otp}"
        send_email_notification(subject, message, instance.email)
        return instance


class ForgotPasswordChangeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = (
            'email',
            'otp',
            'new_password',
            'password_confirmation',
        )

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Электронной почты не существует.")
        return value

    def validate_otp(self, value):
        if len(str(value)) != 5:
            raise serializers.ValidationError("Неверный формат код подтверждения")
        return value


    def validate(self, data):
        new_password = data.get('new_password')
        password_confirmation = data.get('password_confirmation')
        if new_password and new_password != password_confirmation:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        email = validated_data.get('email')
        otp = validated_data.get('otp')
        new_password = validated_data.get('new_password')
        try:
            user = User.objects.get(
                email=email,
                otp=otp
            )
        except User.DoesNotExist:
            raise serializers.ValidationError("Неправильный код")
        user.set_password(new_password)
        user.save()
        return user
