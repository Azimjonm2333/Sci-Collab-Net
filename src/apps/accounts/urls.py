from django.urls import path
from src.apps.accounts.views import (
    RegistrationView,
    ChangePasswordView,
    UserProfileAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),

    # token
    path('token/refresh/', TokenRefreshView.as_view()),

    # profile
    path('clients/profile/', UserProfileAPIView.as_view()),
]
