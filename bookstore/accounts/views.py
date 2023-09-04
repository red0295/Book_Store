from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django_otp import devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice
from accounts.models import User
from accounts.serializers import UserSerializer, SignupSerializer, SigninSerializer
""" from .decorators import admin_only """
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

class SigninView(generics.GenericAPIView):
    serializer_class = SigninSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            if user.otp_secret:
                if 'otp_code' not in serializer.validated_data:
                    return Response({'detail': 'OTP code is required.'}, status=status.HTTP_400_BAD_REQUEST)
                device = next(devices_for_user(user, TOTPDevice), None)
                if not device or not device.verify_token(serializer.validated_data['otp_code']):
                    return Response({'detail': 'Invalid OTP code.'}, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            return Response({'detail': 'Successfully signed in.'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
