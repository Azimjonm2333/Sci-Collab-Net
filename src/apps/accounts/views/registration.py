from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import User, UserProfile
from ..serializers import (
    ChangePasswordSerializer,
    RegistrationSerializer,
    LoginSerializer,
)
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from rest_framework_simplejwt.tokens import RefreshToken
from src.config.settings.base import EMAIL_ACCESS_TOKEN_EXPIRE_MINUTES
from django.http import JsonResponse


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    authentication_classes = []

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            username = request.data.get('username')
            new_password = request.data.get('new_password')

            instance = User.objects.get(username=username)
            instance.set_password(new_password)
            instance.save()

            return Response({
                "detail": "Ваш пароль успешно изменен",
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_confirmation_email(user, request):
    token = urlsafe_base64_encode(force_bytes(f"{user.id}/{datetime.now().timestamp()}"))
    confirmation_url = request.build_absolute_uri(reverse('confirm_email', kwargs={'token': token}))

    subject = 'Подтверждение электронной почты'
    message = f"Перейдите по ссылке {confirmation_url}"
    from_email = 'send.message.2333@gmail.com'
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)


def confirm_email(request, token):
    try:
        decoded_token = force_str(urlsafe_base64_decode(token)).split('/')
        user_id = int(decoded_token[0])
        timestamp = float(decoded_token[1])

        user = User.objects.get(id=user_id)
        EMAIL_ACCESS_TOKEN = timedelta(minutes=int(EMAIL_ACCESS_TOKEN_EXPIRE_MINUTES))

        if datetime.now() - datetime.fromtimestamp(timestamp) < EMAIL_ACCESS_TOKEN:
            message = "Ваша почта уже подтверждена" if user.is_verify else "Ваша почта успешно подтверждена"
            user.is_verify = True
            user.save()
            return JsonResponse({
                "message": message,
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            "message": "Время ссылки истекло",
        }, status=status.HTTP_400_BAD_REQUEST)

    except (ValueError, TypeError, User.DoesNotExist, IndexError) as e:
        print(e)
        return JsonResponse({
            "message": "Bad Request",
        }, status=status.HTTP_400_BAD_REQUEST)


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    authentication_classes = ()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            send_confirmation_email(user, self.request)
            UserProfile.objects.create(
                user=user
            )

            return Response({
                "type": "Bearer",
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login View
class LoginView(APIView):
    authentication_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate the user based on username and password
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                # Generate token or use any authentication method you prefer
                token = "generated_bearer_token"
                return Response({"token": token}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
