from rest_framework import generics
from rest_framework.response import Response
from ..serializers import ForgotPasswordSerializer, ForgotPasswordChangeSerializer
from rest_framework import status



class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    authentication_classes = ()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.is_valid():
            return Response({
                "detail": "Код для восстановления пароля отправлена вам в почту"
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ForgotPasswordChangeView(generics.GenericAPIView):
    serializer_class = ForgotPasswordChangeSerializer
    authentication_classes = ()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer.is_valid():
            return Response({
                "detail": "Вы успешно поменяли пароль"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)