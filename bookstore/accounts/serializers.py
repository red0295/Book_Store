from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'otp_secret']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}

class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    otp_code = serializers.CharField(required=False)
